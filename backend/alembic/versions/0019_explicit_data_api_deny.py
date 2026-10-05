"""make Data API denial explicit on practical tables

Revision ID: 0019
Revises: 0018
Create Date: 2026-10-05

Practical tables are server-only. Explicit false policies preserve the existing
deny-by-default behavior for Supabase Data API roles while making the intent
visible to database tooling and resilient to future privilege drift.
"""

import sqlalchemy as sa

from alembic import op

revision = "0019"
down_revision = "0018"
branch_labels = None
depends_on = None

PRACTICAL_TABLES = (
    "decision_attempts",
    "competence_evidence",
    "life_simulation_sessions",
    "classroom_sessions",
    "classroom_participants",
    "classroom_responses",
    "partnership_interests",
)


def upgrade() -> None:
    if op.get_bind().dialect.name != "postgresql":
        return
    table_array = ", ".join(f"'{table}'" for table in PRACTICAL_TABLES)
    op.execute(
        sa.text(
            f"""
DO $deny$
DECLARE
    table_name text;
BEGIN
    IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'anon')
       AND EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'authenticated') THEN
        FOREACH table_name IN ARRAY ARRAY[{table_array}]
        LOOP
            EXECUTE format(
                'DROP POLICY IF EXISTS academy_data_api_deny ON public.%I',
                table_name
            );
            EXECUTE format(
                'CREATE POLICY academy_data_api_deny ON public.%I '
                'FOR ALL TO anon, authenticated USING (false) WITH CHECK (false)',
                table_name
            );
        END LOOP;
    END IF;
END
$deny$;
"""
        )
    )


def downgrade() -> None:
    if op.get_bind().dialect.name != "postgresql":
        return
    for table in PRACTICAL_TABLES:
        op.execute(sa.text(f"DROP POLICY IF EXISTS academy_data_api_deny ON public.{table}"))

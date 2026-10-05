"""reconcile remote RLS helper hardening

Revision ID: 0016
Revises: 0015
Create Date: 2026-08-03

The linked Supabase project already applied this hardening as
"revoke_public_rls_helper_0016". Keep the Alembic chain aligned with the
authoritative production head without assuming the Supabase helper exists on
plain PostgreSQL used by CI.
"""

import sqlalchemy as sa
from alembic import op

revision = "0016"
down_revision = "0015"
branch_labels = None
depends_on = None


def upgrade() -> None:
    if op.get_bind().dialect.name != "postgresql":
        return
    op.execute(
        sa.text(
            """
DO $hardening$
BEGIN
    IF to_regprocedure('public.rls_auto_enable()') IS NOT NULL THEN
        REVOKE EXECUTE ON FUNCTION public.rls_auto_enable() FROM PUBLIC;
        IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'anon') THEN
            REVOKE EXECUTE ON FUNCTION public.rls_auto_enable() FROM anon;
        END IF;
        IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'authenticated') THEN
            REVOKE EXECUTE ON FUNCTION public.rls_auto_enable() FROM authenticated;
        END IF;
        IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'service_role') THEN
            GRANT EXECUTE ON FUNCTION public.rls_auto_enable() TO service_role;
        END IF;
    END IF;
END
$hardening$;
"""
        )
    )


def downgrade() -> None:
    # Security hardening is intentionally not reversed automatically.
    pass

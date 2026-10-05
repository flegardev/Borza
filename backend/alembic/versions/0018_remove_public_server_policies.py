"""remove broad PUBLIC server policies

Revision ID: 0018
Revises: 0017
Create Date: 2026-10-05

The production database server roles (postgres/service_role) bypass RLS. The
PUBLIC server policy therefore adds planner work for authenticated requests
without providing a required access path. Keep RLS enabled and retain the
owner-scoped authenticated policies.
"""

import sqlalchemy as sa
from alembic import op

revision = "0018"
down_revision = "0017"
branch_labels = None
depends_on = None

TABLES = (
    "users",
    "profiles",
    "user_preferences",
    "onboarding_profiles",
    "enrollments",
    "lesson_progress",
    "lesson_notes",
    "lesson_bookmarks",
    "quiz_attempts",
    "question_responses",
    "review_schedules",
    "flashcard_reviews",
    "user_skill_mastery",
    "simulation_sessions",
    "simulation_orders",
    "simulation_trades",
    "trading_journals",
    "journal_tags",
    "trading_journal_tags",
    "user_achievements",
    "study_streaks",
    "activity_events",
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
    for table in TABLES:
        op.execute(sa.text(f"DROP POLICY IF EXISTS academy_direct_server_access ON public.{table}"))


def downgrade() -> None:
    if op.get_bind().dialect.name != "postgresql":
        return
    for table in TABLES:
        op.execute(
            sa.text(
                f"""
CREATE POLICY academy_direct_server_access ON public.{table}
FOR ALL TO PUBLIC
USING (
    NOT pg_has_role(current_user, 'anon', 'member')
    AND NOT pg_has_role(current_user, 'authenticated', 'member')
)
WITH CHECK (
    NOT pg_has_role(current_user, 'anon', 'member')
    AND NOT pg_has_role(current_user, 'authenticated', 'member')
)
"""
            )
        )

"""add covering indexes for ownership and ingestion foreign keys

Revision ID: 0017
Revises: 0016
Create Date: 2026-10-05
"""

from alembic import op

revision = "0017"
down_revision = "0016"
branch_labels = None
depends_on = None

INDEXES = (
    (
        "ix_classroom_responses_participant_session_fk",
        "classroom_responses",
        ("participant_id", "classroom_session_id"),
    ),
    (
        "ix_flashcard_reviews_schedule_owner_fk",
        "flashcard_reviews",
        ("schedule_id", "user_id"),
    ),
    (
        "ix_question_responses_attempt_owner_fk",
        "question_responses",
        ("attempt_id", "user_id"),
    ),
    ("ix_service_heartbeats_current_job_fk", "service_heartbeats", ("current_job_id",)),
    (
        "ix_simulation_orders_session_owner_fk",
        "simulation_orders",
        ("session_id", "user_id"),
    ),
    (
        "ix_simulation_trades_entry_order_owner_fk",
        "simulation_trades",
        ("entry_order_id", "user_id"),
    ),
    (
        "ix_simulation_trades_session_owner_fk",
        "simulation_trades",
        ("session_id", "user_id"),
    ),
    (
        "ix_trading_journal_tags_journal_owner_fk",
        "trading_journal_tags",
        ("journal_id", "user_id"),
    ),
    (
        "ix_trading_journal_tags_tag_owner_fk",
        "trading_journal_tags",
        ("tag_id", "user_id"),
    ),
    (
        "ix_trading_journals_session_owner_fk",
        "trading_journals",
        ("simulation_session_id", "user_id"),
    ),
)


def upgrade() -> None:
    for name, table, columns in INDEXES:
        op.create_index(name, table, list(columns))


def downgrade() -> None:
    for name, table, _columns in reversed(INDEXES):
        op.drop_index(name, table_name=table)

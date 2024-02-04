"""initialize tables

Revision ID: pe
Revises:
Create Date: 2024-01-27 01:38:09.703308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b10845bded33'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def create_user_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.BIGINT, primary_key=True)
    )


def create_file_info_table() -> None:
    op.create_table(
        "file_info",
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column("filename", sa.String, nullable=False),
        sa.Column("conversion_date", sa.DateTime, nullable=False),
        sa.Column(
            "user_id",
            sa.BIGINT,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False
        )
    )


def upgrade() -> None:
    create_user_table()
    create_file_info_table()


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("file_info")

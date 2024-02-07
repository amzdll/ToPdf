"""replace_ondelete_in_file_info_table

Revision ID: 07e0c99f9afb
Revises: b10845bded33
Create Date: 2024-02-07 19:00:30.990343

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '07e0c99f9afb'
down_revision: Union[str, None] = 'b10845bded33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        'file_info_user_id_fkey',
        'file_info',
        type_='foreignkey'
    )

    op.create_foreign_key(
        'file_info_user_id_fkey',
        'file_info',
        'users',
        ['user_id'],
        ['id'],
        ondelete='NO ACTION'
    )


def downgrade() -> None:
    op.drop_constraint(
        'file_info_user_id_fkey',
        'file_info',
        type_='foreignkey'
    )
    op.create_foreign_key(
        'file_info_user_id_fkey',
        'file_info',
        'users', ['user_id'],
        ['id'],
        ondelete='CASCADE')

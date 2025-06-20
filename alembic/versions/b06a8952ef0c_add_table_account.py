"""add table account

Revision ID: b06a8952ef0c
Revises: 
Create Date: 2025-06-20 11:30:37.143855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b06a8952ef0c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('account', sa.Column('id', sa.Integer, primary_key=True),sa.Column('email',sa.String(30)))


def downgrade() -> None:
    op.drop_table('account')

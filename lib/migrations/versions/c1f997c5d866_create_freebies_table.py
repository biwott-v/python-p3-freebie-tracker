"""create freebies table

Revision ID: c1f997c5d866
Revises: 5f72c58bf48c
Create Date: 2025-06-05 12:32:18.251609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1f997c5d866'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=True),
        sa.Column('value', sa.Integer(), nullable=True),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id')),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('freebies')
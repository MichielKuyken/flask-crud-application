"""entries table

Revision ID: fcf703acee75
Revises: 
Create Date: 2024-03-08 15:50:22.138820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcf703acee75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entry_description'), 'entry', ['description'], unique=False)
    op.create_index(op.f('ix_entry_title'), 'entry', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_entry_title'), table_name='entry')
    op.drop_index(op.f('ix_entry_description'), table_name='entry')
    op.drop_table('entry')
    # ### end Alembic commands ###

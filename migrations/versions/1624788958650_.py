"""empty message

Revision ID: 1624788958650
Revises: 1624742941808
Create Date: 2021-06-27 17:15:59.379262

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1624788958650'
down_revision = '1624742941808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('iteration', sa.Column('status', sa.String(), nullable=False))
    op.drop_column('iteration', 'end_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('iteration', sa.Column('end_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('iteration', 'status')
    # ### end Alembic commands ###

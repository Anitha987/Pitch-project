"""Initial Migration

Revision ID: 311500f4060c
Revises: b2eb825d7b33
Create Date: 2019-09-25 17:05:53.334158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '311500f4060c'
down_revision = 'b2eb825d7b33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

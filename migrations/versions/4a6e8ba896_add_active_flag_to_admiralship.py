"""Add active flag to admiralship

Revision ID: 4a6e8ba896
Revises: 2096dc4473f
Create Date: 2015-05-14 18:54:26.348148

"""

# revision identifiers, used by Alembic.
revision = '4a6e8ba896'
down_revision = '2096dc4473f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admiral_ship', sa.Column('active', sa.Boolean(), nullable=False, server_default="true"))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admiral_ship', 'active')
    ### end Alembic commands ###

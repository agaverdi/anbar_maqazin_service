"""empty message

Revision ID: 9b413d81e5f7
Revises: 3b7f9f378040
Create Date: 2020-08-15 13:08:33.700509

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '9b413d81e5f7'
down_revision = '3b7f9f378040'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'anbar', ['id'])
    op.create_unique_constraint(None, 'category', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_constraint(None, 'anbar', type_='unique')
    # ### end Alembic commands ###

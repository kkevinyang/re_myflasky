"""use avatar

Revision ID: 2c63dc5e5469
Revises: d9f3b4d89c56
Create Date: 2016-08-16 16:09:00.314598

"""

# revision identifiers, used by Alembic.
revision = '2c63dc5e5469'
down_revision = 'd9f3b4d89c56'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
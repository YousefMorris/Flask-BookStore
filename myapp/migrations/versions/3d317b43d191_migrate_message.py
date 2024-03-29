"""migrate message

Revision ID: 3d317b43d191
Revises: 9e965600e57c
Create Date: 2024-02-23 01:17:55.110441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d317b43d191'
down_revision = '9e965600e57c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))
        batch_op.drop_column('Price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Price', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('price')

    # ### end Alembic commands ###

"""agregue tabla categorias

Revision ID: 7a879a8b228c
Revises: 37a532263c5c
Create Date: 2023-03-17 20:32:07.809389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a879a8b228c'
down_revision = '37a532263c5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('imagen', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categorias')
    # ### end Alembic commands ###

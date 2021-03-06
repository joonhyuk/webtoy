"""empty message

Revision ID: 8253b42a9418
Revises: 883afdf98309
Create Date: 2022-02-12 14:59:35.249624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8253b42a9418'
down_revision = '883afdf98309'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###

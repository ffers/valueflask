"""add likes nullable=True

Revision ID: ea25dd205e1c
Revises: d4c3c40cd3a8
Create Date: 2023-09-01 10:43:32.303228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea25dd205e1c'
down_revision = 'd4c3c40cd3a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.alter_column('posts_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('comment_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.alter_column('comment_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('posts_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
"""add users nullable=True

Revision ID: d4c3c40cd3a8
Revises: 95733ae91f47
Create Date: 2023-09-01 10:24:11.886219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4c3c40cd3a8'
down_revision = '95733ae91f47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('author_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('post_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('author_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('author_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('post_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('author_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
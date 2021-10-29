"""Added other models

Revision ID: d593fd345722
Revises: b15317c95186
Create Date: 2021-10-13 20:16:32.268862

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd593fd345722'
down_revision = 'b15317c95186'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('primary_isbn10', sa.Integer(), nullable=False),
                    sa.Column('primary_isbn13', sa.Integer(), nullable=False),
                    sa.Column('publisher', sa.String(length=256), nullable=True),
                    sa.Column('description', sa.String(length=512), nullable=True),
                    sa.Column('price', sa.Float(), nullable=True),
                    sa.Column('title', sa.String(length=256), nullable=True),
                    sa.Column('author', sa.String(length=256), nullable=True),
                    sa.Column('contributor', sa.String(length=256), nullable=True),
                    sa.Column('book_image_url', sa.String(length=256), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('primary_isbn10'),
                    sa.UniqueConstraint('primary_isbn13')
                    )
    op.create_table('carts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('checkout',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('book_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('checkout')
    op.drop_table('carts')
    op.drop_table('book')
    # ### end Alembic commands ###

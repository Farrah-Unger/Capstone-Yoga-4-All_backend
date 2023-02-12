"""updated reflex model with image propert

Revision ID: 98d84287d1d8
Revises: 396887605a5f
Create Date: 2023-02-12 11:24:48.431750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98d84287d1d8'
down_revision = '396887605a5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reflex', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reflex', 'image')
    # ### end Alembic commands ###
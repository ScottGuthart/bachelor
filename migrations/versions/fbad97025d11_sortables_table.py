"""sortables table

Revision ID: fbad97025d11
Revises: 
Create Date: 2019-12-27 14:25:31.143879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbad97025d11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sortables',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sortables')
    # ### end Alembic commands ###

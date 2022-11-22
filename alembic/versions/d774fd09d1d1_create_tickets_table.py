"""Create tickets Table

Revision ID: d774fd09d1d1
Revises: 00193ae1c627
Create Date: 2022-11-22 23:41:23.330357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd774fd09d1d1'
down_revision = '00193ae1c627'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tickets',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('redeemed', sa.Boolean, nullable=False),
        sa.Column('events_id', sa.Integer, sa.ForeignKey('events.id'), nullable=False),
    )

def downgrade():
    op.drop_table('tickets')

"""Create event Table

Revision ID: 00193ae1c627
Revises: 
Create Date: 2022-11-22 23:20:34.683067

"""
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, TIMESTAMP, Column


# revision identifiers, used by Alembic.
revision = '00193ae1c627'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'events',
        Column('id', INTEGER, primary_key=True),
        Column('name', VARCHAR(50), nullable=False),
        Column('date', TIMESTAMP, nullable=False),
    )

def downgrade():
    op.drop_table('events')

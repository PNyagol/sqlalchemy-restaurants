from alembic import op
import sqlalchemy as sa

revision = '[timestamp]'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('restaurants',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True)
    )

    op.create_table('customers',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True)
    )

    op.create_table('reviews',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('star_rating', sa.Integer(), nullable=True),
        sa.Column('restaurant_id', sa.Integer(), sa.ForeignKey('restaurants.id'), nullable=True),
        sa.Column('customer_id', sa.Integer(), sa.ForeignKey('customers.id'), nullable=True)
    )

def downgrade():
    op.drop_table('reviews')
    op.drop_table('customers')
    op.drop_table('restaurants')

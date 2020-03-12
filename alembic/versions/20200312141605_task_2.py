"""Task 2

Revision ID: 4fa581f8bfb6
Revises: 00000000
Create Date: 2020-03-12 14:16:05.281154

"""

# revision identifiers, used by Alembic.
revision = '4fa581f8bfb6'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


"""
2. Write a migration to do the following:
    * Increase the point_balance for user 1 to 5000
    * Add a location for user 2, assuming they live in the USA
    * Change the tier for user 3 to Silver
    
Note: I mimicked the original migration and used raw SQL for this. If I were more familiar with sqlalchemy as
an ORM, I probably would have chosen to write this migration using that instead.
"""


def upgrade():
    op.execute('''UPDATE user
        SET point_balance = 5000
        WHERE user_id = 1;
    ''')

    op.execute('''INSERT INTO rel_user (user_id, rel_lookup, attribute)
        VALUES (2, 'LOCATION', 'USA');
    ''')

    op.execute('''UPDATE user
        SET tier = 'Silver'
        WHERE user_id = 3;
    ''')

def downgrade():
    op.execute('''UPDATE user
        SET point_balance = 0
        WHERE user_id = 1;
    ''')

    op.execute('''DELETE FROM rel_user
        WHERE user_id = 2;
    ''')

    op.execute('''UPDATE user
        SET tier = 'Carbon'
        WHERE user_id = 3;
    ''')


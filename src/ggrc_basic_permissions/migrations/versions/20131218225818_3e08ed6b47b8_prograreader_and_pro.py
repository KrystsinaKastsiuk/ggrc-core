
"""PrograReader and ProgramEditor need to be able to read UserRole resources.

Revision ID: 3e08ed6b47b8
Revises: 2785a204a673
Create Date: 2013-12-18 22:58:18.613406

"""

# revision identifiers, used by Alembic.
revision = '3e08ed6b47b8'
down_revision = '2785a204a673'

import sqlalchemy as sa
from alembic import op
from datetime import datetime
from sqlalchemy.sql import table, column, select
import json

roles_table = table('roles',
    column('id', sa.Integer),
    column('name', sa.String),
    column('permissions_json', sa.String)
    )

def get_role_permissions(role):
  connection = op.get_bind()
  role = connection.execute(
      select([roles_table.c.permissions_json])\
          .where(roles_table.c.name == role)).fetchone()
  return json.loads(role.permissions_json)

def update_role_permissions(role, permissions):
  op.execute(roles_table\
      .update()\
      .values(permissions_json = json.dumps(permissions))\
      .where(roles_table.c.name == role))

def upgrade():
  update_role_permissions('ProgramReader', {
                    "read": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "Program",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship",
                        "ObjectFolder",
                        "UserRole",
                    ],
                    "create": [],
                    "view_object_page": [
                        "__GGRC_ALL__"
                    ],
                    "update": [],
                    "delete": []
                })
  update_role_permissions('ProgramEditor', {
                    "read": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "Program",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship",
                        "ObjectFolder",
                        "UserRole",
                    ],
                    "create": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship",
                        "ObjectFolder"
                    ],
                    "view_object_page": [
                        "__GGRC_ALL__"
                    ],
                    "update": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "Program",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship"
                    ],
                    "delete": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship",
                        "ObjectFolder"
                    ]
                })

def downgrade():
  update_role_permissions('ProgramReader', {
                    "read": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "Program",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship",
                        "ObjectFolder"
                    ],
                    "create": [],
                    "view_object_page": [
                        "__GGRC_ALL__"
                    ],
                    "update": [],
                    "delete": []
                })
  update_role_permissions('ProgramEditor', {
                    "read": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "Program",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship",
                        "ObjectFolder"
                    ],
                    "create": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship",
                        "ObjectFolder"
                    ],
                    "view_object_page": [
                        "__GGRC_ALL__"
                    ],
                    "update": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "Program",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship"
                    ],
                    "delete": [
                        "ObjectDocument",
                        "ObjectObjective",
                        "ObjectPerson",
                        "ObjectSection",
                        "ProgramControl",
                        "ProgramDirective",
                        "Relationship",
                        "ObjectFolder"
                    ]
                })

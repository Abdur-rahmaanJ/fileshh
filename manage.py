import sys

from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager


from init import db

from models import *

migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)

manager.add_command("db", MigrateCommand)


# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade


if __name__ == "__main__":
    manager.run()
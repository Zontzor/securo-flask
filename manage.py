# manage.py

# initialize migrations: python manage.py db init
# run migrations: python manage.py db migrate
# apply migrations: python manage.py db upgrade

import os

# third-party imports
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# local imports
from app import db, create_app
from app import models

app = create_app(config_name=os.getenv('FLASK_CONFIG'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

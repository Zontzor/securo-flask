# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

# function returns correct configuration from config.py
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # initialize db
    db.init_app(app)

    # initialize migration
    migrate = Migrate(app, db)

    from app import models

    return app

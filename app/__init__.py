# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

# login manager initialization
login_manager = LoginManager()

# function returns correct configuration from config.py
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # initialize db
    db.init_app(app)

    # initialize login manager
    login_manager.init_app(app)
    # display specified message
    login_manager.login_message = "You must be logged in to access this page."
    # display specified view
    login_manager.login_view = "auth.login"

    # initialize migration
    migrate = Migrate(app, db)

    from app import models

    return app

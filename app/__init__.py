# app/__init__.py

# third-party imports
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request, jsonify, abort

# local imports
from instance.config import app_config

# db variable initialization
db = SQLAlchemy()

# function returns correct configuration from config.py
def create_app(config_name):
    from app.models import Photo

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize db
    db.init_app(app)

    # initialize migration
    migrate = Migrate(app, db)

    @app.route('/photos/', methods=['POST', 'GET'])
    def photos():
        if request.method == "POST":
            filename = str(request.data.get('filename', ''))
            if filename:
                photo = Photo(filename=filename)
                photo.save()
                response = jsonify({
                    'id': photo.id,
                    'filename': photo.filename,
                    'date_created': photo.date_created,
                    'date_modified': photo.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            photos = Photo.get_all()
            results = []

            for photo in photos:
                obj = {
                    'id': photo.id,
                    'filename': photo.filename,
                    'date_created': photo.date_created,
                    'date_modified': photo.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    return app

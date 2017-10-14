# FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run
import os
from flask import Flask

UPLOAD_FOLDER = 'photos/'
ALLOWED_EXTENSIONS = set(['png'])

app = Flask(__name__)
app.config[UPLOAD_FOLDER] = UPLOAD_FOLDER

@app.route("/")
def hello():
    return 'nada'

@app.route("/get_image")
def read_photo():
    return 'nada'

@app.route("/post_image")
def create_photo():
    return 'nada'

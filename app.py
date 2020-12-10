from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from dotenv import load_dotenv
import os

import models
from resources.users import user
from resources.user_profiles import profile
from resources.manager_user_profiles import manager_profile

load_dotenv()

DEBUG = True
PORT = 8000

app = Flask(__name__)

login_manager = LoginManager()
app.secret_key =  'kEEpItlIkEasEcrEt'
# app.secret_key =  os.getenv('SECRET_KEY')
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.Users.get(models.Users.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

CORS(profile, origins=['*'], supports_credentials=True)
CORS(user, origins=['*'], supports_credentials=True)

app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(user, url_prefix='/users')
app.register_blueprint(manager_profile, url_prefix='/managers')

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
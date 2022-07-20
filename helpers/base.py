import os
from dotenv import load_dotenv
from flask_cors import CORS
from resources.users import user
from resources.user_profiles import profile
from resources.manager_user_profiles import manager_profile

load_dotenv()


def get_env_vars():
    return {
        'secret':  os.environ.get('SECRET_KEY'),
        'port': os.environ.get('PORT'),
        'debug': os.environ.get('DEBUG')
    }


def set_session_cookies_true(app):
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_SAMESITE='None'
    )


def set_cors():
    CORS(profile, origins=['*'], supports_credentials=True)
    CORS(user, origins=['*'], supports_credentials=True)
    CORS(manager_profile, origins=['*'], supports_credentials=True)


def set_register_blueprint(app):
    app.register_blueprint(profile, url_prefix='/profile')
    app.register_blueprint(user, url_prefix='/users')
    app.register_blueprint(manager_profile, url_prefix='/managers')

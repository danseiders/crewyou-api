from playhouse.db_url import connect
from peewee import PostgresqlDatabase
from flask_cors import CORS
from resources.users import user
from resources.user_profiles import profile
from resources.manager_user_profiles import manager_profile
import os
from dotenv import load_dotenv

load_dotenv()


def get_env_vars():
    return {
        'secret':  os.environ.get('SECRET_KEY'),
        'port': os.environ.get('PORT'),
        'debug': os.environ.get('DEBUG'),
        'environment': os.environ.get('ENVIRONMENT'),
        'db_url': os.environ.get('DATABASE_URL')
    }


def set_session_cookies(app):
    env_vars = get_env_vars()

    if env_vars['environment'] == 'prod':
        app.config.update(
            SESSION_COOKIE_SECURE=True,
            SESSION_COOKIE_SAMESITE='None'
        )
        print('session cookies set')


def set_cors():
    CORS(profile, origins=['*'], supports_credentials=True)
    CORS(user, origins=['*'], supports_credentials=True)
    CORS(manager_profile, origins=['*'], supports_credentials=True)


def set_register_blueprint(app):
    app.register_blueprint(profile, url_prefix='/profile')
    app.register_blueprint(user, url_prefix='/users')
    app.register_blueprint(manager_profile, url_prefix='/managers')


def get_db():
    env_vars = get_env_vars()

    if env_vars['environment'] == 'prod':
        response = connect(env_vars['db_url'])
    elif env_vars['environment'] == 'dev':
        response = PostgresqlDatabase('crewyou')

    return response

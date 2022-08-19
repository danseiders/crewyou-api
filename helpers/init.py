import logging
import os
import helpers.app_config as config_helper
from flask_cors import CORS
from logging.config import dictConfig
from resources.users.user_controller import user
from resources.profiles.profiles import profile
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
        logging.info('session cookies set')


def set_cors():
    CORS(profile, origins=['*'], supports_credentials=True)
    CORS(user, origins=['*'], supports_credentials=True)


def set_register_blueprint(app):
    app.register_blueprint(profile, url_prefix='/profile')
    app.register_blueprint(user, url_prefix='/user')


def set_dynamo_tables(app):
    app.config['DYNAMO_TABLES'] = config_helper.get_db_config()


def set_logging_config(app):
    dictConfig(config_helper.get_logger_config())
    logging.info('LOGGING CONFIG SET')


def get_users():
    return user

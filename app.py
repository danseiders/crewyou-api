import helpers.init as init
from flask import Flask
from flask_login import LoginManager
from flask_dynamo import Dynamo
import logging

app = Flask(__name__)
login_manager = LoginManager()
dynamo = Dynamo(app)


def set_init_app():
    app.secret_key = env_vars['secret']
    login_manager.init_app(app)
    init.set_cors()
    init.set_register_blueprint(app)
    init.set_session_cookies(app)
    init.set_dynamo_tables(app)
    init.set_logging_config(app)


@login_manager.user_loader
def load_user(user_id):
    user = init.get_users()

    return user.get(user_id)


if __name__ == '__main__':
    env_vars = init.get_env_vars()
    set_init_app()

    with app.app_context():
        dynamo = Dynamo(app)
        dynamo.create_all()
        logging.info('Created Tables')

    logging.info(app.url_map)
    app.run(debug=env_vars['debug'], port=env_vars['port'])

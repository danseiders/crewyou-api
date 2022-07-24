import resources.models as models
import helpers.init as init
from flask import Flask, g
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()


def set_init_app():
    app.secret_key = env_vars['secret']
    login_manager.init_app(app)
    init.set_cors()
    init.set_register_blueprint(app)
    init.set_session_cookies(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        return models.Users.get(models.Users.id == user_id)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    print('connected to db')


@app.after_request
def after_request(response):
    g.db.close()
    return response


if __name__ == '__main__':
    env_vars = init.get_env_vars()
    set_init_app()

    models.initialize()
    app.run(debug=env_vars['debug'], port=env_vars['port'])

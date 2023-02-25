import app
from flask_login import UserMixin
import helpers.requests as request


class User:
    def __init__(self, user):
        self.username = user['username']
        self.email = user['email']
        self.password = user['password']

    def set_new_user_id(user):
        user.id = request.get_uuid()

    def set_user_type(user, type):
        user.type = type

    def set_user_is_active(user, bool):
        user.is_active = bool

    def set_user_is_active(user, bool):
        user.is_authenticated = bool

    def get(user):
        return app.dynamo.tables['users'].get_item(
            Key={
                'email': user.email
            }
        )

    def put(user):
        return app.dynamo.tables['users'].put_item(Item=user.__dict__)

    def patch(user):
        return app.dynamo.tables['users'].update_item(Item=user.__dict__)

    def delete(user):
        return app.dynamo.tables['users'].put_item(Item=user.__dict__)

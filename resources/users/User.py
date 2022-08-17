import app
from flask_login import UserMixin
import helpers.requests as request


class User:
    def __init__(self, user):
        print('SELF', user)
        self.id = request.get_uuid()
        self.username = user['username']
        self.email = user['email']
        self.password = user['password']
        self.user_type = user['user_type']
        self.is_active = False
        self.is_authenticated = False

    def get(user):
        return app.dynamo.tables['users'].get_item(
            Key={
                'email': user.email
            }
        )

    def put(user):
        return app.dynamo.tables['users'].put_item(Item=user.__dict__)

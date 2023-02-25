import app
import logging
import boto3
import helpers.requests as RequestHelper
import helpers.responses as ResponseHelper
import resources.users.user_class as UserClass
import resources.middleware.requests as RequestMiddleware
from flask import Blueprint, request

user = Blueprint('user', __name__)


def _get_parsed_username_and_pass(payload):
    return {
        'username': payload['username'],
        'password': RequestHelper.get_password_hash(payload['password']),
    }


def _get_parsed_new_user_payload(payload):
    user = _get_parsed_username_and_pass(payload)

    return {
        'email': payload['email'].lower(),
        'username': user['username'],
        'password': user['password'],
        'user_type': payload['user_type'],
        'is_active': False
    }


def get(payload):
    payload = _get_parsed_username_and_pass(payload)
    user = UserClass(payload)
    user.get()

    return '200'


def put(payload):
    payload = _get_parsed_new_user_payload(payload)
    user = UserClass.User(payload)
    print(user.__dict__)

    app.dynamo.tables['users'].put_item(Item=user.__dict__)

    return '200'


def patch(payload):
    return 'PATCH USER'


def delete(payload):
    return '200'


@user.route('', methods=['GET'])
def get_user():
    return RequestMiddleware.get_response(request)


@user.route('', methods=['PUT'])
def create_user():
    return RequestMiddleware.get_response(request)


@user.route('', methods=['PATCH'])
def update_user():
    return RequestMiddleware.get_response(request)


@user.route('', methods=['DELETE'])
def delete_user():
    return RequestMiddleware.get_response(request)

    # except Exception as e:
    #     app.logging.exception(e)
    # else:

    # try:
    #     models.User.get(models.User.email == payload['email'])

    #     return jsonify(data={}, status={'code': 401, 'message': 'A user with that name already exists'})

    # except models.DoesNotExist:
    #     payload['password'] = generate_password_hash(payload['password'])
    #     user = models.Users.create(**payload)
    #     login_user(user)
    #     user_dict = model_to_dict(user)
    #     print(user_dict)
    #     print(type(user_dict))
    #     del user_dict['password']
    #     return jsonify(data=user_dict, status={'code': 201, 'message': 'Success'})

    # @ user.route('/login', methods=['POST'])
    # def login():
    #     payload = request.get_json()
    #     payload['email'] = [payload['email'].lower()]
    #     print('payload', payload)
    #     try:
    #     user = models.Users.get(models.Users.email == payload['email'])
    #     user_dict = model_to_dict(user)
    #     if(check_password_hash(user_dict['password'], payload['password'])):
    #         del user_dict['password']
    #         login_user(user)
    #         print(user, 'this is user')
    #         return jsonify(data=user_dict, status={'code': 200, 'message': 'Success'})
    #     else:
    #         print('Username or Password is incorrect')
    #         return jsonify(data={}, status={'code': 401, 'message': 'Username or Password is incorrect'
    #                                         })
    #     except models.DoesNotExist:
    #     print('User does not exist')
    #     return jsonify(data={}, status={'code': 401, 'message': 'Username or Password is incorrect'})

    #     @ user.route('/logout', methods=['GET'])
    #     def logout():
    #     logout_user()
    #     return jsonify(data={}, status={'code': 200, 'message': 'Successful logout'})

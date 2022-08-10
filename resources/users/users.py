import app
import logging
import helpers.requests as request_helper
import helpers.responses as responses
from urllib import response
from flask import Blueprint, jsonify, request
from flask_login import login_user, logout_user
from playhouse.shortcuts import model_to_dict
from flask_dynamo import Dynamo

user = Blueprint('user', __name__)


def _is_user(email):
    response = app.dynamo.tables['users'].get_item(
        Key={
            'email': email
        }
    )

    return response


def _parse_payload(payload):
    return {
        'email': payload['email'].lower(),
        'username': payload['username'],
        'password': request_helper.get_password_hash(payload['password']),
        'user_type': payload['user_type'],
        'is_active': False
    }


@user.route('', methods=['POST'])
def create_user():
    payload = _parse_payload(request.json)
    logging.info(payload)

    if 'Item' in _is_user(payload['email']):
        status_code = '409'
    else:
        print(app.dynamo.tables['users'].put_item(Item=payload))
        status_code = '200'
        # login_user(payload)

    return responses.get_response(request, status_code)

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

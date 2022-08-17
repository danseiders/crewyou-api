import app
import logging
import helpers.requests as request_helper
import helpers.responses as response_helper
from flask import Blueprint, jsonify, request
from flask_login import login_user, logout_user
from playhouse.shortcuts import model_to_dict
from flask_dynamo import Dynamo
import resources.users.User as UserClass

user = Blueprint('user', __name__)


def _get_parsed_payload(payload):
    return {
        'email': payload['email'].lower(),
        'username': payload['username'],
        'password': request_helper.get_password_hash(payload['password']),
        'user_type': payload['user_type'],
        'is_active': False
    }


def _get_get_response(user):
    return 'GET!'


def _get_put_response(user):
    if 'Item' in user.get():
        status_code = '409'
    else:
        user.put()
        status_code = '200'

    return status_code


def _get_patch_response(user):
    return 'PATCH!'


def _get_delete_response(user):
    return 'DELETE!'


def _get_response(request):
    user = UserClass.User(_get_parsed_payload(request.json))
    logging.info(user)
    response = {
        'GET': _get_get_response(user),
        'PUT': _get_put_response(user),
        'PATCH': _get_patch_response(user),
        'DELETE': _get_delete_response(user)
    }

    return response_helper.get_response(request, response[request.method])


@user.route('', methods=['PUT'])
def create_user():
    try:
        response = _get_response(request)

    except Exception as e:
        print('FUCKING ERRRORRR')
        response = str(e)

    finally:
        return response


@user.route('', methods=['GET'])
def get_user():
    return _get_response(request)


@user.route('', methods=['PATCH'])
def update_user():
    return _get_response(request)


@user.route('', methods=['DELETE'])
def delete_user():
    return _get_response(request)
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

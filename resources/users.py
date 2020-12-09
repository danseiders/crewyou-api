import models
from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user')

@user.route('/new', methods=['POST'])
def create_user():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    try:
        models.Users.get(models.Users.email == payload['email'])
        return jsonify(data={}, status={'code': 401, 'message': 'A user with that name already exists'})
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        user = models.Users.create(**payload)
        login_user(user)
        user_dict = model_to_dict(user)
        print(user_dict)
        print(type(user_dict))
        del user_dict['password']
        return jsonify(data=user_dict, status={'code': 201, 'message': 'Success'})

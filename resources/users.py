import models
from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
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

@user.route('/login', methods=['POST'])
def login():
    payload= request.get_json()
    payload['email'] = [payload['email'].lower()]
    print('payload', payload)
    try:
        user = models.Users.get(models.Users.email == payload['email'])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            print(user, 'this is user')
            return jsonify(data=user_dict, status={'code': 200, 'message': 'Success'})
        else:
            print('Username or Password is in correct')
            return jsonify(data={}, status={'code': 401, 'message': 'Username or Password is incorrect'
            })
    except models.DoesNotExist:
        print('User does not exist')
        return jsonify(data={}, status={'code': 401, 'message': 'Username or Password is incorrect'})
        
@user.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return jsonify(data={}, status={'code': 200, 'message': 'Successful logout'})
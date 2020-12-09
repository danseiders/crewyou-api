import models
from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user')

@user.route('/new', methods=['POST'])
def create_user():
    payload = request.get_json()
    print(type(payload), 'payload')
    user = models.Users.create(**payload)
    print(user.__dict__)
    print(dir(user))
    print(model_to_dict(user), 'model to dict')
    user = model_to_dict(user)
    return jsonify(data=user_dict, status={'code': 201, 'message': 'Sucess'})

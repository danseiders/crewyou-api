import models
from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

profile = Blueprint('user_profiles', 'user_profile')

# @user.route('/', methods=['GET'])
# def create_user():
#     payload = request.get_json()
#     print(type(payload), 'payload')
#     user_profile = models.UserProfile.create(**payload)
#     print(user.__dict__)
#     print(dir(user_profile))
#     print(model_to_dict(user_profile), 'model to dict')
#     user_profile_dict = model_to_dict(user_profile)
#     return jsonify(data=user_profile_dict, status={'code': 201, 'message': 'Sucess'})

@profile.route('/new', methods=['POST'])
def create_user():
    payload = request.get_json()
    print(type(payload), 'payload')
    user_profile = models.Profiles.create(**payload)
    print(user_profile.__dict__)
    print(dir(user_profile))
    print(model_to_dict(user_profile), 'model to dict')
    user_profile_dict = model_to_dict(user_profile)
    return jsonify(data=user_profile_dict, status={'code': 201, 'message': 'Sucess'})

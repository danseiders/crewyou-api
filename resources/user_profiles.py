import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

profile = Blueprint('user_profiles', 'user_profile')

@profile.route('/', methods=['GET'])
@login_required
def get_all_profiles():
    try:
        profiles = [model_to_dict(profile) for profile in current_user.profiles]
        print(profiles)
        return jsonify(data=profiles, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resources'})

@profile.route('/', methods=['POST'])
def create_profile():
    print(request)
    payload = request.get_json()
    print(payload)
    payload['user_id'] = current_user.id
    # print(type(payload), 'payload')
    user_profile = models.Profiles.create(**payload)
    # print(user_profile.__dict__)
    # print(dir(user_profile))
    # print(model_to_dict(user_profile), 'model to dict')
    user_profile_dict = model_to_dict(user_profile)
    return jsonify(data=user_profile_dict, status={'code': 201, 'message': 'Sucess'})

@profile.route('/<id>', methods=['PUT'])
def edit_profile(id):
    print(request)
    print(id)
    payload = request.get_json()
    print(payload)
    query = models.Profiles.update(**payload).where(models.Profiles.id==id)
    print(query)
    query.execute()
    return jsonify(data=model_to_dict(models.Profiles.get_by_id(id)), status={'code': 200, 'message':'resource updated successfully'})
    return 'hello'

@profile.route('/<id>', methods=['DELETE'])
def delete_profile(id):
    query = models.Profiles.delete().where(models.Profiles.id==id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={'code': 200, 'message': 'resource deleted successfully'})

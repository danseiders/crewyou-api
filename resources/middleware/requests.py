import logging
import json
from posixpath import split
import resources.profiles.profiles as profile
import helpers.responses as ResponseHelper
import resources.users.user_controller as user


def _get_path(request):
    path = '/{}'.format(request.path.split('/')[1])

    response = {
        '/user': user,
        '/profile': profile,

    }

    return response[path]


def _get_get_response(request, path):
    # payload = request.json
    return path.get(request)


def _get_put_response(request, path):
    # payload = request.json
    return path.put(request)


def _get_post_response(payload, path):
    return path.post(payload)


def _get_patch_response(payload, path):
    return path.patch(payload)


def _get_delete_response(payload, path):
    return path.delete(payload)


def get_response(request):
    path = _get_path(request)
    json_request = request.json

    try:
        response = {
            'GET': _get_get_response,
            'PUT': _get_put_response,
            'POST': _get_post_response,
            'PATCH': _get_patch_response,
            'DELETE': _get_delete_response
        }

        response = response[request.method](json_request, path)

    except Exception as e:
        response = '500'
        err = str(e)
    finally:
        return ResponseHelper.get(request, response, err='')

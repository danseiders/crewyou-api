import logging
import resources.profiles.profiles as profile
import helpers.responses as ResponseHelper
import resources.users.user_controller as user


def _get_path(request):
    response = {
        '/user': user,
        '/profile': profile,
    }

    return response[request.path]


def _get_get_response(request, path):
    return path.get(request)


def _get_put_response(request, path):
    return path.put(request)


def _get_post_response(request, path):
    return path.post(request)


def _get_patch_response(request, path):
    return path.patch(request)


def _get_delete_response(request, path):
    return path.delete(request)


def get_response(request):
    path = _get_path(request)
    try:
        response = {
            'GET': _get_get_response(request, path),
            'PUT': _get_put_response(request, path),
            'POST': _get_post_response(request, path),
            'PATCH': _get_patch_response(request, path),
            'DELETE': _get_delete_response(request, path)
        }

        response = response[request.method]

    except Exception as e:
        response = str(e)
    finally:
        return response
        # return ResponseHelper.get_response(request, response[request.method])

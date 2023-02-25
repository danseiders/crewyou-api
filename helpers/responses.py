from email import message
import logging
from flask import jsonify


def _get_user_response_message(request, status_code, err):
    response = {
        'PUT': {
            '200': 'User successfully created',
            '409': 'User already exists',
            '500': 'Server Error: {}'.format(err)
        },
        'DELETE': {
            '200': 'User successfully deleted',
            '400': 'User does not exist'
        }
    }

    return response[request.method][status_code]


def _get_response_message(request, status_code, err):
    path = '/{}'.format(request.path.split('/')[1])

    responses = {
        '/user': _get_user_response_message
    }

    return responses[path](request, status_code, err)


def get(request, status_code, err=''):
    return jsonify({
        'status': status_code,
        'message': _get_response_message(request, status_code, err)
    })

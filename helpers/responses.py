import logging
from flask import jsonify


def _get_response_message(request, status_code):
    responses = {
        '/user': {
            'PUT': {
                '200': 'User successfully created',
                '409': 'User already exists'
            }
        }
    }
    logging.info(responses[request.path][request.method][status_code])

    return responses[request.path][request.method][status_code]


def get_response(request, status_code):
    return jsonify({
        'status': status_code,
        'message': _get_response_message(request, status_code)
    })

from functools import wraps
import os
from flask import request
import jwt
from helpers.responses import error_response
from models.user import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            message = 'Bad request. Header does not contain an authorization token'
            error_response['message'] = message
            return error_response, 401

        try:
            decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'))
        except:
            error_response['message'] = 'Bad request. The provided token is invalid'
            return error_response, 401
        setattr(request, 'decoded_token', decoded_token)
        return f(*args, **kwargs)
    return decorated

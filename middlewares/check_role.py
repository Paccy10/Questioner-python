from functools import wraps
from flask import request
from models.user import User
from schemas.user import UserSchema
from helpers.responses import error_response
from .token_required import token_required


def check_role(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        decoded_token = request.decoded_token
        current_user = User.query.filter_by(id=decoded_token['user']).first()
        user_schema = UserSchema(strict=True)
        user_data = user_schema.dump(current_user).data
        if not user_data['is_admin']:
            message = 'Permission denied. You are not authorized to perform this action'
            error_response['message'] = message
            return error_response, 403

        return f(*args, **kwargs)
    return decorated

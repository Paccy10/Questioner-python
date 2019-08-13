import re
import datetime
from models.user import User
from helpers.responses import error_response


class UserValidors:

    @classmethod
    def signup_validator(cls, data: dict):
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if not firstname or not firstname.strip():
            error_response['message'] = 'The firstname is required'
            return error_response, 400

        if not lastname or not lastname.strip():
            error_response['message'] = 'The lastname is required'
            return error_response, 400

        if not email or not email.strip():
            error_response['message'] = 'The email is required'
            return error_response, 400

        if not re.match(email_regex, email):
            error_response['message'] = 'The email provided is not valid'
            return error_response, 400

        if User.query.filter(User.email == email).first():
            error_response['message'] = 'The email provided already exists'
            return error_response, 400

        if not password or not password.strip():
            error_response['message'] = 'The password is required'
            return error_response, 400

        if len(password.strip()) < 6:
            error_response['message'] = 'Password must be at least 6 characters'
            return error_response, 400

    @classmethod
    def login_validator(cls, data: dict):
        email = data.get('email')
        password = data.get('password')
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if not email or not email.strip():
            error_response['message'] = 'The email is required'
            return error_response, 400

        if not re.match(email_regex, email):
            error_response['message'] = 'The email provided is not valid'
            return error_response, 400

        if not password or not password.strip():
            error_response['message'] = 'The password is required'
            return error_response, 400

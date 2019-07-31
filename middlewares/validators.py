import re
from models.user import User


class UserValidors:

    @classmethod
    def signup_validator(cls, data: dict):
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        response = {
            'status': 'error',
            'message': '',
        }

        if not firstname or not firstname.strip():
            response['message'] = 'The firstname is required.'
            return response, 400

        if not lastname or not lastname.strip():
            response['message'] = 'The lastname is required.'
            return response, 400

        if not email or not email.strip():
            response['message'] = 'The email is required.'
            return response, 400

        if not re.match(email_regex, email):
            response['message'] = 'The email provided is not valid.'
            return response, 400

        if User.query.filter(User.email == email).first():
            response['message'] = 'The email provided already exists.'
            return response, 400

        if not password or not password.strip():
            response['message'] = 'The password is required.'
            return response, 400

        if len(password.strip()) < 6:
            response['message'] = 'Password must be at least 6 characters.'
            return response, 400

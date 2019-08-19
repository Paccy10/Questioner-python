import re
import datetime
from models.user import User
from helpers.responses import error_response
from .error import raise_validation_error


class UserValidors:

    @classmethod
    def signup_validator(cls, data: dict):
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if not firstname or not firstname.strip():
            raise_validation_error('The firstname is required')

        if not lastname or not lastname.strip():
            raise_validation_error('The lastname is required')

        if not email or not email.strip():
            raise_validation_error('The email is required')

        if not re.match(email_regex, email):
            raise_validation_error('The email provided is not valid')

        if User.query.filter(User.email == email).first():
            raise_validation_error('The email provided already exists')

        if not password or not password.strip():
            raise_validation_error('The password is required')

        if len(password.strip()) < 6:
            raise_validation_error('Password must be at least 6 characters')

    @classmethod
    def login_validator(cls, data: dict):
        email = data.get('email')
        password = data.get('password')
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if not email or not email.strip():
            raise_validation_error('The email is required')

        if not re.match(email_regex, email):
            raise_validation_error('The email provided is not valid')

        if not password or not password.strip():
            raise_validation_error('The password is required')

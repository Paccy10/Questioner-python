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


class MeetupValidators:

    @classmethod
    def meetup_validator(cls, data: dict):
        topic = data.get('topic')
        location = data.get('location')
        happening_on = data.get('happening_on')

        if not topic or not topic.strip():
            error_response['message'] = 'The topic is required'
            return error_response, 400

        if not location or not location.strip():
            error_response['message'] = 'The location is required'
            return error_response, 400

        if not happening_on or not happening_on.strip():
            error_response['message'] = 'The happening_on date is required'
            return error_response, 400

        try:
            datetime.datetime.strptime(happening_on, '%Y-%m-%d')
            print(datetime.date.today())
        except ValueError:
            error_response['message'] = 'Invalid date format. It should be like YYYY-MM-DD'
            return error_response, 400

        if datetime.datetime.strptime(happening_on, '%Y-%m-%d').date() < datetime.date.today():
            message = 'Invalid date. The date should be greater or equal to today\'s date'
            error_response['message'] = message
            return error_response, 400

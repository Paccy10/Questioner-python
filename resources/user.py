from flask import request
import bcrypt
from flask_restplus import Resource
from server.instance import server
from models.user import User
from models.database import db
from schemas.user import UserSchema
from middlewares.validators import UserValidors
from helpers.generate_token import generate_token
from helpers.responses import success_response, error_response

api = server.api


@api.route('/api/auth/signup')
class UserSignupResource(Resource):

    def post(self):
        """"Endpoint to create a user"""

        user_schema = UserSchema(strict=True, exclude=['password'])
        request_data = request.get_json()
        validation_error = UserValidors.signup_validator(request_data)
        if validation_error:
            return validation_error
        bytes_password = bytes(request_data['password'], encoding='utf-8')
        hashed = bcrypt.hashpw(bytes_password, bcrypt.gensalt(10))
        request_data['password'] = hashed.decode('utf-8')

        new_user = User(**request_data)
        new_user.save()

        token = generate_token(user_schema.dump(new_user).data['id'])
        success_response['message'] = 'User successfully created'
        success_response['data'] = {
            'token': token,
            'user': user_schema.dump(new_user).data
        }

        return success_response, 201


@api.route('/api/auth/login')
class UserLoginResource(Resource):
    def post(self):
        """"Endpoint to login a user"""

        user_schema = UserSchema(strict=True)
        request_data = request.get_json()
        validation_error = UserValidors.login_validator(request_data)

        if validation_error:
            return validation_error
        email = request_data['email']
        password = bytes(request_data['password'], encoding='utf-8')
        user = User.query.filter(User.email == email).first()
        error_response['message'] = 'Incorrect username or password'

        if user:
            user_data = user_schema.dump(user).data
            hashed = bytes(user_data['password'], encoding='utf-8')
            if bcrypt.checkpw(password, hashed):
                token = generate_token(user_data['id'])
                success_response['message'] = 'User successfully logged in'
                success_response['data'] = {
                    'token': token
                }
                return success_response, 200
            return error_response, 404
        return error_response, 404

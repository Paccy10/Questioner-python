from flask import request
import bcrypt
from flask_restplus import Resource
from models.user import User
from schemas.user import UserSchema
from helpers.swagger.collections import user_namespace
from helpers.swagger.models import user_model
from helpers.validators.user import UserValidors
from helpers.generate_token import generate_token
from helpers.responses import success_response, error_response
from helpers.request_data_strip import request_data_strip


@user_namespace.route('/signup')
class UserSignupResource(Resource):

    @user_namespace.expect(user_model)
    def post(self):
        """"Endpoint to create a user"""

        user_schema = UserSchema(exclude=['password', 'deleted_at', 'deleted'])
        request_data = request.get_json()
        UserValidors.signup_validator(request_data)

        request_data = request_data_strip(request_data)

        bytes_password = bytes(request_data['password'], encoding='utf-8')
        hashed = bcrypt.hashpw(bytes_password, bcrypt.gensalt(10))
        request_data['password'] = hashed.decode('utf-8')

        new_user = User(**request_data)
        new_user.save()

        token = generate_token(user_schema.dump(new_user)['id'])
        success_response['message'] = 'User successfully created'
        success_response['data'] = {
            'token': token,
            'user': user_schema.dump(new_user)
        }

        return success_response, 201


@user_namespace.route('/login')
class UserLoginResource(Resource):

    @user_namespace.expect(user_model)
    def post(self):
        """"Endpoint to login a user"""

        user_schema = UserSchema()
        request_data = request.get_json()
        UserValidors.login_validator(request_data)

        request_data = request_data_strip(request_data)

        email = request_data['email']
        password = bytes(request_data['password'], encoding='utf-8')
        user = User.query.filter(User.email == email).first()
        error_response['message'] = 'Incorrect username or password'

        if user:
            user_data = user_schema.dump(user)
            hashed = bytes(user_data['password'], encoding='utf-8')
            if bcrypt.checkpw(password, hashed):
                token = generate_token(user_data['id'])
                user_schema = UserSchema(
                    exclude=['password', 'deleted_at', 'deleted'])
                logged_in_user = user_schema.dump(user)
                success_response['message'] = 'User successfully logged in'
                success_response['data'] = {
                    'token': token,
                    'user': logged_in_user
                }
                return success_response, 200
            return error_response, 404
        return error_response, 404

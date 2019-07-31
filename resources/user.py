from flask import request
import bcrypt
from flask_restplus import Resource
from server.instance import server
from models.user import User
from models.database import db
from schemas.user import UserSchema
from middlewares.validators import UserValidors
from helpers.generate_token import generate_token

api = server.api
user_schema = UserSchema(strict=True)


@api.route('/api/auth/signup')
class UserSignup(Resource):

    def post(self):
        request_data = request.get_json()
        validation_error = UserValidors.signup_validator(request_data)
        if validation_error:
            return validation_error
        bytes_password = bytes(request_data['password'], encoding='utf-8')
        hashed = bcrypt.hashpw(bytes_password, bcrypt.gensalt(10))
        request_data['password'] = hashed

        new_user = User(**request_data)
        db.session.add(new_user)
        db.session.commit()

        token = generate_token(user_schema.dump(new_user).data['id'])

        return {
            "status": "success",
            "message": "User successfully created",
            "data": {
                "token": token,
                "user": user_schema.dump(new_user).data
            }
        }, 201

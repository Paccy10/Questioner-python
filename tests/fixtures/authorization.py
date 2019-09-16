import pytest
from flask import json
from models.database import db
from schemas.user import UserSchema
from helpers.generate_token import generate_token
import resources.user
from tests.mocks.user import LOGIN_USER_DATA_TO_GET_TOKEN
from tests.helpers.constants import (CHARSET, CONTENT_TYPE)


@pytest.fixture(scope='module')
def user_auth_header(init_db, new_user):
    new_user.save()

    user_schema = UserSchema()
    user_data = user_schema.dump(new_user)
    token = generate_token(user_data)
    return {
        'Authorization': token,
        'Content-Type': 'application/json'
    }


@pytest.fixture(scope='module')
def admin_auth_header(init_db, new_admin):
    new_admin.save()

    user_schema = UserSchema()
    user_data = user_schema.dump(new_admin)
    token = generate_token(user_data)
    return {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

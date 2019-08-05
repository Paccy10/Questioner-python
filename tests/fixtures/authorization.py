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
    db.session.add(new_user)
    db.session.commit()

    user_schema = UserSchema(strict=True)
    user_data = user_schema.dump(new_user).data
    token = generate_token(user_data['id'])
    return {
        'Authorization': token,
        'Content-Type': 'application/json'
    }


@pytest.fixture(scope='module')
def admin_auth_header(init_db, new_admin):
    db.session.add(new_admin)
    db.session.commit()

    user_schema = UserSchema(strict=True)
    user_data = user_schema.dump(new_admin).data
    token = generate_token(user_data['id'])
    return {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

from flask import json
from tests.helpers.constants import (CHARSET, CONTENT_TYPE)
from tests.mocks.user import (
    VALID_USER, INVALID_USER_WITHOUT_FIRSTNAME,
    INVALID_USER_WITHOUT_LASTNAME,
    INVALID_USER_WITHOUT_EMAIL,
    INVALID_USER_WITHOUT_PASSWORD,
    INVALID_USER_WITH_INVALID_EMAIL,
    INVALID_USER_WITH_INVALID_PASSWORD)
import resources.user


class TestUserEndpoints:
    """Class for testing user resource"""

    def test_user_signup_succeeds(self, client, init_db):
        user_data = json.dumps(VALID_USER)
        response = client.post(
            '/api/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'User successfully created'
        assert 'token' in response.json['data']
        assert 'user' in response.json['data']
        assert response.json['data']['user']['email'] == VALID_USER['email']

    def test_user_signup_without_firstname_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITHOUT_FIRSTNAME)
        response = client.post(
            '/api/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The firstname is required.'

    def test_user_signup_without_lastname_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITHOUT_LASTNAME)
        response = client.post(
            '/api/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The lastname is required.'

    def test_user_signup_without_email_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITHOUT_EMAIL)
        response = client.post(
            '/api/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The email is required.'

    def test_user_signup_without_password_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITHOUT_PASSWORD)
        response = client.post(
            '/api/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The password is required.'

    def test_user_signup_with_an_invalid_email_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITH_INVALID_EMAIL)
        response = client.post(
            '/api/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The email provided is not valid.'

    def test_user_signup_with_an_existing_email_fails(self, client, init_db):
        user_data = json.dumps(VALID_USER)
        response = client.post(
            '/api/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The email provided already exists.'

    def test_user_signup_with_an_invalid_password_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITH_INVALID_PASSWORD)
        response = client.post(
            '/api/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Password must be at least 6 characters.'

from flask import json
from tests.helpers.constants import (CONTENT_TYPE)
from tests.mocks.user import (
    VALID_USER, INVALID_USER_WITHOUT_FIRSTNAME,
    INVALID_USER_WITHOUT_LASTNAME,
    INVALID_USER_WITHOUT_EMAIL,
    INVALID_USER_WITHOUT_PASSWORD,
    INVALID_USER_WITH_INVALID_EMAIL,
    INVALID_USER_WITH_INVALID_PASSWORD,
    LOGIN_USER_DATA,
    LOGIN_USER_DATA_WITHOUT_EMAIL,
    LOGIN_USER_DATA_INVALID_EMAIL,
    LOGIN_USER_DATA_WITHOUT_PASSWORD,
    LOGIN_UNREGISTERED_USER,
    LOGIN_USER_DATA_WITH_INCORRECT_PASSWORD)
import resources.user

API_BASE_URL = '/api/v1'


class TestUserEndpoints:
    """Class for testing user resource"""

    def test_user_signup_succeeds(self, client, init_db):
        user_data = json.dumps(VALID_USER)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'User successfully created'
        assert 'token' in response.json['data']
        assert 'user' in response.json['data']
        assert response.json['data']['user']['email'] == VALID_USER['email']

    def test_user_signup_without_firstname_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITHOUT_FIRSTNAME)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The firstname is required'

    def test_user_signup_without_lastname_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITHOUT_LASTNAME)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The lastname is required'

    def test_user_signup_without_email_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITHOUT_EMAIL)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The email is required'

    def test_user_signup_without_password_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITHOUT_PASSWORD)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The password is required'

    def test_user_signup_with_an_invalid_email_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITH_INVALID_EMAIL)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The email provided is not valid'

    def test_user_signup_with_an_existing_email_fails(self, client, init_db):
        user_data = json.dumps(VALID_USER)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The email provided already exists'

    def test_user_signup_with_an_invalid_password_fails(self, client, init_db):
        user_data = json.dumps(INVALID_USER_WITH_INVALID_PASSWORD)
        response = client.post(
            f'{API_BASE_URL}/auth/signup', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Password must be at least 6 characters'

    def test_user_login_succeeds(self, client, init_db):
        user_data = json.dumps(LOGIN_USER_DATA)
        response = client.post(
            f'{API_BASE_URL}/auth/login', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'User successfully logged in'
        assert 'token' in response.json['data']

    def test_user_login_without_email_fails(self, client, init_db):
        user_data = json.dumps(LOGIN_USER_DATA_WITHOUT_EMAIL)
        response = client.post(
            f'{API_BASE_URL}/auth/login', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The email is required'

    def test_user_login_with_invalid_email_fails(self, client, init_db):
        user_data = json.dumps(LOGIN_USER_DATA_INVALID_EMAIL)
        response = client.post(
            f'{API_BASE_URL}/auth/login', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The email provided is not valid'

    def test_user_login_without_password_fails(self, client, init_db):
        user_data = json.dumps(LOGIN_USER_DATA_WITHOUT_PASSWORD)
        response = client.post(
            f'{API_BASE_URL}/auth/login', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The password is required'

    def test_user_login_with_incorrect_password_fails(self, client, init_db):
        user_data = json.dumps(LOGIN_USER_DATA_WITH_INCORRECT_PASSWORD)
        response = client.post(
            f'{API_BASE_URL}/auth/login', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Incorrect username or password'

    def test_unregistered_user_login_fails(self, client, init_db):
        user_data = json.dumps(LOGIN_UNREGISTERED_USER)
        response = client.post(
            f'{API_BASE_URL}/auth/login', data=user_data, content_type=CONTENT_TYPE)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Incorrect username or password'

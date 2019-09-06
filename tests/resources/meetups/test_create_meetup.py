from flask import json
from tests.mocks.meetup import (
    VALID_MEETUP,
    INVALID_MEETUP_WITHOUT_TOPIC,
    INVALID_MEETUP_WITHOUT_LOCATION,
    INVALID_MEETUP_WITHOUT_DATE,
    INVALID_MEETUP_WITH_INVALID_DATE_FORMAT,
    INVALID_MEETUP_WITH_INVALID_DATE
)
from tests.helpers.constants import CONTENT_TYPE
import resources.meetup

API_BASE_URL = '/api/v1'
class TestCreateMeetup:
    """Class for testing create meetup endpoint"""

    def test_create_meetup_succeeds(self, client, init_db, admin_auth_header):
        meetup_data = json.dumps(VALID_MEETUP)
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, headers=admin_auth_header)

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Meetup successfully created'
        assert 'meetup' in response.json['data']
        assert response.json['data']['meetup']['topic'] == VALID_MEETUP['topic']

    def test_create_meetup_without_auth_token_fails(self, client, init_db):
        meetup_data = json.dumps(VALID_MEETUP)
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, content_type=CONTENT_TYPE)
        message = 'Bad request. Header does not contain an authorization token'
        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_meetup_with_invalid_auth_token_fails(self, client, init_db):
        meetup_data = json.dumps(VALID_MEETUP)
        headers = {
            'Authorization': 'andela',
            'Content_type': CONTENT_TYPE
        }
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, headers=headers)
        message = 'Bad request. The provided token is invalid'
        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_meetup_with_a_non_admin_user_fails(self, client, init_db, user_auth_header):
        meetup_data = json.dumps(VALID_MEETUP)
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, headers=user_auth_header)
        message = 'Permission denied. You are not authorized to perform this action'
        assert response.status_code == 403
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_meetup_without_topic_fails(self, client, init_db, admin_auth_header):
        meetup_data = json.dumps(INVALID_MEETUP_WITHOUT_TOPIC)
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, headers=admin_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The topic is required'

    def test_create_meetup_without_location_fails(self, client, init_db, admin_auth_header):
        meetup_data = json.dumps(INVALID_MEETUP_WITHOUT_LOCATION)
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, headers=admin_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The location is required'

    def test_create_meetup_without_date_fails(self, client, init_db, admin_auth_header):
        meetup_data = json.dumps(INVALID_MEETUP_WITHOUT_DATE)
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, headers=admin_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The happening_on date is required'

    def test_create_meetup_with_invalid_date_format_fails(self, client, init_db, admin_auth_header):
        meetup_data = json.dumps(INVALID_MEETUP_WITH_INVALID_DATE_FORMAT)
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, headers=admin_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Invalid date format. It should be like YYYY-MM-DD'

    def test_create_meetup_with_invalid_date_fails(self, client, init_db, admin_auth_header):
        meetup_data = json.dumps(INVALID_MEETUP_WITH_INVALID_DATE)
        response = client.post(
            f'{API_BASE_URL}/meetups', data=meetup_data, headers=admin_auth_header)

        message = 'Invalid date. The date should be greater or equal to today\'s date'
        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

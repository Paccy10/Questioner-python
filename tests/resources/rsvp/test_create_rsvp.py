from flask import json
from tests.mocks.rsvp import (
    VALID_RSVP,
    ANOTHER_VALID_RSVP,
    INVALID_RSVP_WITHOUT_RESPONSE,
    INVALID_RSVP_WITH_INVALID_RESPONSE
)
from tests.helpers.constants import CONTENT_TYPE
import resources.rsvp

API_BASE_URL = '/api/v1'


class TestCreateRsvp:
    """Class for testing create rsvp endpoint"""

    def test_create_rsvp_succeeds(self, client, init_db, new_meetup, user_auth_header):
        new_meetup.save()
        rsvp_data = json.dumps(VALID_RSVP)
        response = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps',
            data=rsvp_data, headers=user_auth_header)

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Rsvp successfully created'
        assert 'rsvp' in response.json['data']
        assert response.json['data']['rsvp']['response'] == VALID_RSVP['response']

    def test_create_rsvp_without_auth_token_fails(self, client, init_db, new_meetup):
        new_meetup.save()
        rsvp_data = json.dumps(VALID_RSVP)
        response = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps',
            data=rsvp_data, content_type=CONTENT_TYPE)
        message = 'Bad request. Header does not contain an authorization token'
        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_rsvp_with_invalid_auth_token_fails(self, client, init_db, new_meetup):
        new_meetup.save()
        rsvp_data = json.dumps(VALID_RSVP)
        headers = {
            'Authorization': 'andela',
            'Content_type': CONTENT_TYPE
        }
        response = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps', data=rsvp_data, headers=headers)

        message = 'Bad request. The provided token is invalid'

        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_rsvp_with_invalid_meetup_id_fails(self,
                                                      client,
                                                      init_db,
                                                      user_auth_header):
        rsvp_data = json.dumps(VALID_RSVP)
        response = client.post(
            f'{API_BASE_URL}/meetups/2/rsvps', data=rsvp_data, headers=user_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Meetup not found'

    def test_create_rsvp_without_response_fails(self,
                                                client,
                                                init_db,
                                                new_meetup,
                                                user_auth_header):
        new_meetup.save()
        rsvp_data = json.dumps(INVALID_RSVP_WITHOUT_RESPONSE)
        response = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps',
            data=rsvp_data, headers=user_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The response is required'

    def test_create_rsvp_with_invalid_response_fails(self,
                                                     client,
                                                     init_db,
                                                     new_meetup,
                                                     user_auth_header):
        new_meetup.save()
        rsvp_data = json.dumps(INVALID_RSVP_WITH_INVALID_RESPONSE)
        response = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps',
            data=rsvp_data, headers=user_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == "The response should be 'Yes', 'No' or 'Maybe'"

    def test_update_rsvp_with_the_same_response_fails(self,
                                                      client,
                                                      init_db,
                                                      new_meetup,
                                                      user_auth_header):
        new_meetup.save()
        rsvp_data = json.dumps(VALID_RSVP)
        response = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps',
            data=rsvp_data, headers=user_auth_header)

        response2 = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps',
            data=rsvp_data, headers=user_auth_header)

        assert response2.status_code == 400
        assert response2.json['status'] == 'error'
        assert response2.json['message'] == 'Sorry, you have already responded with that response'

    def test_update_rsvp_succeeds(self,
                                  client,
                                  init_db,
                                  new_meetup,
                                  user_auth_header):
        new_meetup.save()
        rsvp_data = json.dumps(VALID_RSVP)
        rsvp_data2 = json.dumps(ANOTHER_VALID_RSVP)
        response = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps',
            data=rsvp_data, headers=user_auth_header)

        response2 = client.post(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps',
            data=rsvp_data2, headers=user_auth_header)

        assert response2.status_code == 200
        assert response2.json['status'] == 'success'
        assert response2.json['message'] == 'Rsvp successfully updated'
        assert 'rsvp' in response2.json['data']
        assert response2.json['data']['rsvp']['response'] == ANOTHER_VALID_RSVP['response']

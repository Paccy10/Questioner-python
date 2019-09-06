from flask import json
from tests.mocks.meetup import (
    VALID_IMAGES,
    INVALID_IMAGES,
    INVALID_STRING_IMAGES
)
from tests.helpers.constants import CONTENT_TYPE
import resources.meetup

API_BASE_URL = '/api/v1'


class TestAddIMagesToMeetup:
    """Class for testing add images to meetup endpoint"""

    def test_add_add_images_to_meetup_succeeds(self,
                                               client,
                                               init_db,
                                               new_meetup,
                                               admin_auth_header):
        new_meetup.save()
        images_data = json.dumps(VALID_IMAGES)
        response = client.patch(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/images',
            data=images_data, headers=admin_auth_header)

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Images successfully added'
        assert 'meetup' in response.json['data']
        assert response.json['data']['meetup']['images'] == VALID_IMAGES['images']

    def test_add_images_to_meetup_without_auth_token_fails(self, client, init_db, new_meetup):
        new_meetup.save()
        images_data = json.dumps(VALID_IMAGES)
        response = client.patch(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/images',
            data=images_data, content_type=CONTENT_TYPE)

        message = 'Bad request. Header does not contain an authorization token'
        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_add_images_to_meetup_with_invalid_auth_token_fails(self, client, init_db, new_meetup):
        new_meetup.save()
        images_data = json.dumps(VALID_IMAGES)
        headers = {
            'Authorization': 'andela',
            'Content_type': CONTENT_TYPE
        }
        response = client.patch(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/images', data=images_data, headers=headers)

        message = 'Bad request. The provided token is invalid'
        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_add_images_to_meetup_with_a_non_admin_user_fails(self,
                                                              client,
                                                              init_db,
                                                              new_meetup,
                                                              user_auth_header):
        new_meetup.save()
        images_data = json.dumps(VALID_IMAGES)
        response = client.patch(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/images',
            data=images_data, headers=user_auth_header)

        message = 'Permission denied. You are not authorized to perform this action'
        assert response.status_code == 403
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_add_images_to_meetup_with_invalid_meetup_id_fails(self,
                                                               client,
                                                               init_db,
                                                               admin_auth_header):
        images_data = json.dumps(VALID_IMAGES)
        response = client.patch(
            f'{API_BASE_URL}/meetups/2/images',
            data=images_data, headers=admin_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Meetup not found'

    def test_add_images_to_meetup_without_images_fails(self,
                                                       client,
                                                       init_db,
                                                       new_meetup,
                                                       admin_auth_header):
        new_meetup.save()
        images_data = json.dumps(INVALID_IMAGES)
        response = client.patch(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/images',
            data=images_data, headers=admin_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The images are required'

    def test_add_images_to_meetup_with_string_images_fails(self,
                                                           client,
                                                           init_db,
                                                           new_meetup,
                                                           admin_auth_header):
        new_meetup.save()
        images_data = json.dumps(INVALID_STRING_IMAGES)
        response = client.patch(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/images',
            data=images_data, headers=admin_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The images should be an array'

from flask import json
from tests.mocks.question import (
    VALID_QUESTION,
    INVALID_QUESTION_WITHOUT_TITLE,
    INVALID_QUESTION_WITHOUT_BODY
)
from tests.helpers.constants import CONTENT_TYPE
import resources.question


class TestCreateQuestion:
    """Class for testing create question endpoint"""

    def test_create_question_succeeds(self, client, init_db, new_meetup, user_auth_header):
        new_meetup.save()
        question_data = json.dumps(VALID_QUESTION)
        response = client.post(
            f'/api/meetups/{new_meetup.id}/questions',
            data=question_data, headers=user_auth_header)

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Question successfully created'
        assert 'question' in response.json['data']
        assert response.json['data']['question']['title'] == VALID_QUESTION['title']

    def test_create_question_without_auth_token_fails(self, client, init_db, new_meetup):
        new_meetup.save()
        question_data = json.dumps(VALID_QUESTION)
        response = client.post(
            f'/api/meetups/{new_meetup.id}/questions',
            data=question_data, content_type=CONTENT_TYPE)
        message = 'Bad request. Header does not contain an authorization token'
        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_question_with_invalid_auth_token_fails(self, client, init_db, new_meetup):
        new_meetup.save()
        question_data = json.dumps(VALID_QUESTION)
        headers = {
            'Authorization': 'andela',
            'Content_type': CONTENT_TYPE
        }
        response = client.post(
            f'/api/meetups/{new_meetup.id}/questions',
            data=question_data, headers=headers)

        message = 'Bad request. The provided token is invalid'

        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_question_with_invalid_meetup_id_fails(self,
                                                          client,
                                                          init_db,
                                                          user_auth_header):
        question_data = json.dumps(VALID_QUESTION)
        response = client.post(
            f'/api/meetups/2/questions',
            data=question_data, headers=user_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Meetup not found'

    def test_create_question_without_title_fails(self,
                                                 client,
                                                 init_db,
                                                 new_meetup,
                                                 user_auth_header):
        new_meetup.save()
        question_data = json.dumps(INVALID_QUESTION_WITHOUT_TITLE)
        response = client.post(
            f'/api/meetups/{new_meetup.id}/questions',
            data=question_data, headers=user_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The title is required'

    def test_create_question_without_body_fails(self,
                                                client,
                                                init_db,
                                                new_meetup,
                                                user_auth_header):
        new_meetup.save()
        question_data = json.dumps(INVALID_QUESTION_WITHOUT_BODY)
        response = client.post(
            f'/api/meetups/{new_meetup.id}/questions',
            data=question_data, headers=user_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The body is required'

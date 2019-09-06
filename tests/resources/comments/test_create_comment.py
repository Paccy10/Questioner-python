from flask import json
from tests.mocks.comment import (
    VALID_COMMENT,
    INVALID_COMMENT_WITHOUT_BODY
)
from tests.helpers.constants import CONTENT_TYPE
import resources.comment

API_BASE_URL = '/api/v1'


class TestCreateComment:
    """Class for testing create comment endpoint"""

    def test_create_comment_succeeds(self, client, init_db, new_question, user_auth_header):
        new_question.save()
        comment_data = json.dumps(VALID_COMMENT)
        response = client.post(
            f'{API_BASE_URL}/questions/{new_question.id}/comments',
            data=comment_data, headers=user_auth_header)

        assert response.status_code == 201
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Comment successfully created'
        assert 'comment' in response.json['data']
        assert response.json['data']['comment']['body'] == VALID_COMMENT['body']

    def test_create_comment_without_auth_token_fails(self, client, init_db, new_question):
        new_question.save()
        comment_data = json.dumps(VALID_COMMENT)
        response = client.post(
            f'{API_BASE_URL}/questions/{new_question.id}/comments',
            data=comment_data, content_type=CONTENT_TYPE)
        message = 'Bad request. Header does not contain an authorization token'
        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_comment_with_invalid_auth_token_fails(self, client, init_db, new_question):
        new_question.save()
        comment_data = json.dumps(VALID_COMMENT)
        headers = {
            'Authorization': 'andela',
            'Content_type': CONTENT_TYPE
        }
        response = client.post(
            f'{API_BASE_URL}/questions/{new_question.id}/comments',
            data=comment_data, headers=headers)

        message = 'Bad request. The provided token is invalid'

        assert response.status_code == 401
        assert response.json['status'] == 'error'
        assert response.json['message'] == message

    def test_create_comment_with_invalid_question_id_fails(self,
                                                           client,
                                                           init_db,
                                                           user_auth_header):
        comment_data = json.dumps(VALID_COMMENT)
        response = client.post(
            f'{API_BASE_URL}/questions/2/comments',
            data=comment_data, headers=user_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Question not found'

    def test_create_comment_without_body_fails(self,
                                               client,
                                               init_db,
                                               new_question,
                                               user_auth_header):
        new_question.save()
        comment_data = json.dumps(INVALID_COMMENT_WITHOUT_BODY)
        response = client.post(
            f'{API_BASE_URL}/questions/{new_question.id}/comments',
            data=comment_data, headers=user_auth_header)

        assert response.status_code == 400
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'The body is required'

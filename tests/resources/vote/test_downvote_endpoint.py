from flask import json
from tests.helpers.constants import CONTENT_TYPE
import resources.vote

API_BASE_URL = '/api/v1'


class TestDownvoteEndpoint:
    """Class for testing downvote resource"""

    def test_question_downvote_succeeds(self, client, init_db, new_question, user_auth_header):
        new_question.save()
        response = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/downvote', headers=user_auth_header)

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Question successfully downvoted'
        assert 'question' in response.json['data']
        assert response.json['data']['question']['title'] == new_question.title

    def test_question_downvote_with_invalid_question_id_fails(self,
                                                              client,
                                                              init_db,
                                                              user_auth_header):
        response = client.patch(
            f'{API_BASE_URL}/questions/2/downvote', headers=user_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Question not found'

    def test_question_downvote_with_someone_who_already_downvoted_fails(self,
                                                                        client,
                                                                        init_db,
                                                                        new_question,
                                                                        user_auth_header):
        new_question.save()
        response = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/downvote', headers=user_auth_header)

        response2 = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/downvote', headers=user_auth_header)

        assert response2.status_code == 400
        assert response2.json['status'] == 'error'
        assert response2.json['message'] == 'Sorry, you have already downvoted this question'

    def test_question_downvote_with_upvoted_question_succeeds(self,
                                                              client,
                                                              init_db,
                                                              new_question,
                                                              user_auth_header):
        new_question.save()
        response = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/upvote', headers=user_auth_header)

        response2 = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/downvote', headers=user_auth_header)

        assert response2.status_code == 200
        assert response2.json['status'] == 'success'
        assert response2.json['message'] == 'Question successfully downvoted'
        assert 'question' in response2.json['data']
        assert response2.json['data']['question']['title'] == new_question.title

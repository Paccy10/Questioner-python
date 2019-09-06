from flask import json
from tests.helpers.constants import CONTENT_TYPE
import resources.vote

API_BASE_URL = '/api/v1'


class TestUpvoteEndpoint:
    """Class for testing upvote resource"""

    def test_question_upvote_succeeds(self, client, init_db, new_question, user_auth_header):
        new_question.save()
        response = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/upvote', headers=user_auth_header)

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Question successfully upvoted'
        assert 'question' in response.json['data']
        assert response.json['data']['question']['body'] == new_question.body

    def test_question_upvote_with_invalid_question_id_fails(self,
                                                            client,
                                                            init_db,
                                                            user_auth_header):
        response = client.patch(
            f'{API_BASE_URL}/questions/2/upvote', headers=user_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Question not found'

    def test_question_upvote_with_someone_who_already_upvoted_fails(self,
                                                                    client,
                                                                    init_db,
                                                                    new_question,
                                                                    user_auth_header):
        new_question.save()
        response = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/upvote', headers=user_auth_header)

        response2 = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/upvote', headers=user_auth_header)

        assert response2.status_code == 400
        assert response2.json['status'] == 'error'
        assert response2.json['message'] == 'Sorry, you have already upvoted this question'

    def test_question_upvote_with_downvoted_question_succeeds(self,
                                                              client,
                                                              init_db,
                                                              new_question,
                                                              user_auth_header):
        new_question.save()
        response = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/downvote', headers=user_auth_header)

        response2 = client.patch(
            f'{API_BASE_URL}/questions/{new_question.id}/upvote', headers=user_auth_header)

        assert response2.status_code == 200
        assert response2.json['status'] == 'success'
        assert response2.json['message'] == 'Question successfully upvoted'
        assert 'question' in response2.json['data']
        assert response2.json['data']['question']['body'] == new_question.body

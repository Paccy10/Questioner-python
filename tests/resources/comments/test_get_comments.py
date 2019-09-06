import resources.comment

API_BASE_URL = '/api/v1'


class TestGetAllComments:
    """"Class for testing get all comments endpoint"""

    def test_get_all_comments_succeeds(self,
                                       client,
                                       init_db,
                                       new_question,
                                       new_comment,
                                       user_auth_header):
        new_question.save()
        new_comment.save()

        response = client.get(
            f'{API_BASE_URL}/questions/{new_question.id}/comments', headers=user_auth_header)

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Comments successfully fetched'
        assert 'comments' in response.json['data']
        assert len(response.json['data']['comments']) == 1
        assert response.json['data']['comments'][0]['question_id'] == new_question.id

    def test_get_all_comments_with_invalid_question_id_fails(self,
                                                             client,
                                                             init_db,
                                                             user_auth_header):
        response = client.get(
            f'{API_BASE_URL}/questions/2/comments', headers=user_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Question not found'

import resources.question

API_BASE_URL = '/api/v1'


class TestGetAllQuestions:
    """"Class for testing get all questions endpoint"""

    def test_get_all_questions_succeeds(self,
                                        client,
                                        init_db,
                                        new_meetup,
                                        new_question,
                                        user_auth_header):
        new_meetup.save()
        new_question.save()

        response = client.get(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/questions', headers=user_auth_header)

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Questions successfully fetched'
        assert 'questions' in response.json['data']
        assert len(response.json['data']['questions']) == 1
        assert response.json['data']['questions'][0]['meetup_id'] == new_meetup.id

    def test_get_all_questions_with_invalid_meetup_id_fails(self,
                                                            client,
                                                            init_db,
                                                            user_auth_header):
        response = client.get(
            f'{API_BASE_URL}/meetups/2/questions', headers=user_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Meetup not found'

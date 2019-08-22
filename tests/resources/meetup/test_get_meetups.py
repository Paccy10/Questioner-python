import resources.meetup

API_BASE_URL = '/api/v1'


class TestGetAllMeetups:
    """"Class for testing get all meetups endpoint"""

    def test_get_all_meetups_succeeds(self, client, init_db, new_meetup):
        new_meetup.save()

        response = client.get(f'{API_BASE_URL}/meetups')

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Meetups successfully fetched'
        assert 'meetups' in response.json['data']
        assert len(response.json['data']['meetups']) == 1
        assert response.json['data']['meetups'][0]['topic'] == new_meetup.topic

    def test_get_single_meetup_succeeds(self, client, init_db, new_meetup):
        new_meetup.save()

        response = client.get(f'{API_BASE_URL}/meetups/{new_meetup.id}')

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Meetup successfully fetched'
        assert 'meetup' in response.json['data']
        assert response.json['data']['meetup']['topic'] == new_meetup.topic

    def test_get_single_meetup_with_invalid_id_fails(self, client, init_db, new_meetup):
        new_meetup.save()

        response = client.get(f'{API_BASE_URL}/meetups/2')

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Meetup not found'

    def test_get_all_upcoming_meetups_succeeds(self, client, init_db, new_meetup):
        new_meetup.save()

        response = client.get(f'{API_BASE_URL}/meetups/upcoming')

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Upcoming meetups successfully fetched'
        assert 'meetups' in response.json['data']
        assert len(response.json['data']['meetups']) == 1
        assert response.json['data']['meetups'][0]['topic'] == new_meetup.topic

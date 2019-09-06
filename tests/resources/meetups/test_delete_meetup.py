from flask import json
import resources.meetup

API_BASE_URL = '/api/v1'


class TestDeleteMeetup:
    """Class for testing delete meetup endpoint"""

    def test_delete_meetup_succeeds(self, client, init_db, new_meetup, admin_auth_header):
        new_meetup.save()
        response = client.delete(
            f'{API_BASE_URL}/meetups/{new_meetup.id}', headers=admin_auth_header)

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Meetup successfully deleted'
        assert 'meetup' in response.json['data']
        assert 'deleted_at' in response.json['data']['meetup']
        assert response.json['data']['meetup']['deleted'] == True

    def test_delete_meetup_with_inalid_meetup_id_fails(self, client, init_db, admin_auth_header):
        response = client.delete(
            f'{API_BASE_URL}/meetups/2', headers=admin_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Meetup not found'

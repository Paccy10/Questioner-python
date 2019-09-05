import resources.rsvp

API_BASE_URL = '/api/v1'


class TestGetAllRsvps:
    """"Class for testing get all rsvps endpoint"""

    def test_get_all_rsvps_succeeds(self,
                                    client,
                                    init_db,
                                    new_meetup,
                                    new_rsvp,
                                    user_auth_header):
        new_meetup.save()
        new_rsvp.save()

        response = client.get(
            f'{API_BASE_URL}/meetups/{new_meetup.id}/rsvps', headers=user_auth_header)

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Rsvps successfully fetched'
        assert 'rsvps' in response.json['data']
        assert len(response.json['data']['rsvps']) == 1
        assert response.json['data']['rsvps'][0]['meetup_id'] == new_meetup.id

    def test_get_all_rsvps_with_invalid_meetup_id_fails(self,
                                                        client,
                                                        init_db,
                                                        user_auth_header):
        response = client.get(
            f'{API_BASE_URL}/meetups/2/rsvps', headers=user_auth_header)

        assert response.status_code == 404
        assert response.json['status'] == 'error'
        assert response.json['message'] == 'Meetup not found'

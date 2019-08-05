import resources.meetup
from models.database import db


class TestGetAllMeetups:
    """"Class for testing get all meetups endpoint"""

    def test_get_all_meetups_succeeds(self, client, init_db, new_meetup):
        db.session.add(new_meetup)
        db.session.commit()

        response = client.get('/api/meetups')

        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['message'] == 'Meetups successfully fetched'
        assert 'meetups' in response.json['data']
        assert len(response.json['data']['meetups']) == 1

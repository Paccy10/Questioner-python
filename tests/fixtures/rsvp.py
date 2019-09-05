import pytest
from models.rsvp import Rsvp


@pytest.fixture(scope='module')
def new_rsvp(init_db, new_user, new_meetup):
    new_user.save()
    new_meetup.save()
    return Rsvp(
        response='Yes',
        user_id=new_user.id,
        meetup_id=new_meetup.id
    )

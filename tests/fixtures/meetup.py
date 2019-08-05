import pytest
from models.meetup import Meetup


@pytest.fixture(scope='module')
def new_meetup(init_db):
    return Meetup(
        topic='Test Meetup',
        location='Andela Kigali',
        happening_on='2050-08-06',
        images=['image1', 'image2'],
        tags=['tag1', 'tag2'],
    )

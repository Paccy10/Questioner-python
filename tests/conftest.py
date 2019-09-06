import pytest
from server.instance import application
from models.database import db


pytest_plugins = ['tests.fixtures.user',
                  'tests.fixtures.authorization',
                  'tests.fixtures.meetup',
                  'tests.fixtures.question',
                  'tests.fixtures.rsvp',
                  'tests.fixtures.comment']


@pytest.fixture(scope='module')
def app():
    return application


@pytest.fixture(scope='module')
def init_db():
    db.drop_all()
    db.create_all()
    yield db
    db.session.close()

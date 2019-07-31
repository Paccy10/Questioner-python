import pytest
from server.instance import server
from models.database import db


pytest_plugins = []


@pytest.fixture(scope='module')
def app():
    app = server.app
    return app


@pytest.fixture(scope='module')
def init_db():
    db.drop_all()
    db.create_all()
    yield db
    db.session.close()

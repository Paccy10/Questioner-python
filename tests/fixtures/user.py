import pytest
from models.user import User


@pytest.fixture(scope='module')
def new_user(init_db):
    return User(
        firstname='Test',
        lastname='User',
        othername='',
        email='test.user@questioner.com',
        password='Password',
    )


@pytest.fixture(scope='module')
def new_admin(init_db):
    return User(
        firstname='Test',
        lastname='Admin',
        othername='',
        email='test.admin@questioner.com',
        password='Password',
        is_admin=True
    )

import pytest
from models.question import Question


@pytest.fixture(scope='module')
def new_question(init_db, new_user, new_meetup):
    new_user.save()
    new_meetup.save()
    return Question(
        title='Test question',
        body='Test question body',
        user_id=new_user.id,
        meetup_id=new_meetup.id
    )

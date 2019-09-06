import pytest
from models.comment import Comment


@pytest.fixture(scope='module')
def new_comment(init_db, new_user, new_question):
    new_user.save()
    new_question.save()
    return Comment(
        body='Good point',
        user_id=new_user.id,
        question_id=new_question.id
    )

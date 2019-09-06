from models.question import Question
from schemas.question import QuestionSchema

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


def get_question(question_id):
    question_schema = QuestionSchema(exclude=EXCLUDED_FIELDS)
    question = question_schema.dump(
        Question.query.filter_by(id=question_id, deleted=False).first())

    return question

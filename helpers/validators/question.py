from .error import raise_validation_error


class QuestionValidators:

    @classmethod
    def question_validator(cls, data: dict):
        title = data.get('title')
        body = data.get('body')

        if not title or not title.strip():
            raise_validation_error('The title is required')

        if not body or not body.strip():
            raise_validation_error('The body is required')

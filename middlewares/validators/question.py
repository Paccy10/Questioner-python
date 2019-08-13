from helpers.responses import error_response


class QuestionValidators:

    @classmethod
    def question_validator(cls, data: dict):
        title = data.get('title')
        body = data.get('body')

        if not title or not title.strip():
            error_response['message'] = 'The title is required'
            return error_response, 400

        if not body or not body.strip():
            error_response['message'] = 'The body is required'
            return error_response, 400

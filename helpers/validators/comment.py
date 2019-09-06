from .error import raise_validation_error


class CommentValidators:

    @classmethod
    def comment_validator(cls, data: dict):
        body = data.get('body')

        if not body or not body.strip():
            raise_validation_error('The body is required')

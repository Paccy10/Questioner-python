from flask import request
from flask_restplus import Resource
from models.comment import Comment
from schemas.comment import CommentSchema
from middlewares.token_required import token_required
from helpers.swagger.collections import question_namespace
from helpers.swagger.models import comment_model
from helpers.validators.comment import CommentValidators
from helpers.responses import success_response, error_response
from helpers.question import get_question
from helpers.request_data_strip import request_data_strip

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


@question_namespace.route('/<int:question_id>/comments')
class CommentResource(Resource):
    @token_required
    @question_namespace.expect(comment_model)
    def post(self, question_id):
        """Endpoint to create a comment"""

        question = get_question(question_id)

        if not question:
            error_response['message'] = 'Question not found'
            return error_response, 404

        request_data = request.get_json()
        CommentValidators.comment_validator(request_data)

        request_data = request_data_strip(request_data)

        request_data.update(
            {
                'user_id': request.decoded_token['user']['id'],
                'question_id': question_id
            }
        )

        new_comment = Comment(**request_data)
        new_comment.save()
        comment_schema = CommentSchema(exclude=EXCLUDED_FIELDS)
        success_response['message'] = 'Comment successfully created'
        success_response['data'] = {
            'comment': comment_schema.dump(new_comment)
        }

        return success_response, 201

    @token_required
    def get(self, question_id):
        """"Endpoint to get all comments"""

        question = get_question(question_id)

        if not question:
            error_response['message'] = 'Question not found'
            return error_response, 404

        comments_schema = CommentSchema(many=True, exclude=EXCLUDED_FIELDS)
        comments = comments_schema.dump(
            Comment.query.filter(Comment.question_id == question_id, Comment.deleted == False))
        success_response['message'] = 'Comments successfully fetched'
        success_response['data'] = {
            'comments': comments
        }

        return success_response, 200

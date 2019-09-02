from flask import request
from flask_restplus import Resource
from models.question import Question
from models.vote import Vote
from schemas.question import QuestionSchema
from schemas.vote import VoteSchema
from middlewares.token_required import token_required
from helpers.responses import success_response, error_response
from helpers.swagger.collections import question_namespace
from helpers.get_votes import get_votes

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


@question_namespace.route('/<int:question_id>/upvote')
class UpvoteResource(Resource):
    @token_required
    def patch(self, question_id):
        """Endpoint to upvote a question"""
        question_schema = QuestionSchema(exclude=EXCLUDED_FIELDS)
        question = question_schema.dump(
            Question.query.filter_by(id=question_id, deleted=False).first())

        if not question:
            error_response['message'] = 'Question not found'
            return error_response, 404

        vote_schema = VoteSchema(exclude=EXCLUDED_FIELDS)
        vote = vote_schema.dump(Vote.query.filter(
            Vote.user_id == request.decoded_token['user'],
            Vote.question_id == question_id).first())
        vote_data = {
            'user_id': request.decoded_token['user'],
            'question_id': question_id,
            'upvote': True,
            'downvote': False
        }

        if vote:
            if vote['upvote'] == True:
                error_response['message'] = 'Sorry, you have already upvoted this question'
                return error_response, 400

            else:
                vote.update(vote_data)
                votes = get_votes(question_id)
                question.update(votes)
                success_response['message'] = 'Question successfully upvoted'
                success_response['data'] = {
                    'question': question
                }
                return success_response, 200
        else:
            new_vote = Vote(**vote_data)
            new_vote.save()
            votes = get_votes(question_id)
            question.update(votes)
            success_response['message'] = 'Question successfully upvoted'
            success_response['data'] = {
                'question': question
            }
            return success_response, 200
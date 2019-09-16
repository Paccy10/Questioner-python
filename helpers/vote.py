from flask import request
from models.vote import Vote
from schemas.vote import VoteSchema
from helpers.responses import success_response, error_response

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


def get_votes(question_id):
    upvotes = 0
    downvotes = 0
    votes_schema = VoteSchema(many=True, exclude=EXCLUDED_FIELDS)
    question_votes = votes_schema.dump(Vote.query.filter(
        Vote.question_id == question_id))
    for vote in question_votes:
        if vote['upvote']:
            upvotes += 1

        if vote['downvote']:
            downvotes += 1

    return {
        'upvotes': upvotes,
        'downvotes': downvotes
    }


def get_vote(question_id):
    vote = Vote.query.filter(
        Vote.user_id == request.decoded_token['user']['id'],
        Vote.question_id == question_id).first()

    return vote


def update_vote(question_id, question, vote, vote_type, action, vote_data):
    if getattr(vote, vote_type):
        error_response['message'] = f'Sorry, you have already {action} this question'
        return error_response, 400

    else:
        vote.update(vote_data)
        votes = get_votes(question_id)
        question.update(votes)
        success_response['message'] = f'Question successfully {action}'
        success_response['data'] = {
            'question': question
        }
        return success_response, 200

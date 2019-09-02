from models.vote import Vote
from schemas.vote import VoteSchema

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


def get_votes(question_id):
    votes_schema = VoteSchema(many=True, exclude=EXCLUDED_FIELDS)
    upvotes = len(votes_schema.dump(Vote.query.filter(
        Vote.question_id == question_id, Vote.upvote == True)))

    downvotes = len(votes_schema.dump(Vote.query.filter(
        Vote.question_id == question_id, Vote.downvote == True)))

    return {
        'upvotes': upvotes,
        'downvotes': downvotes
    }

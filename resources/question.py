from flask import request
from flask_restplus import Resource
from models.question import Question
from models.meetup import Meetup
from schemas.question import QuestionSchema
from schemas.meetup import MeetupSchema
from middlewares.token_required import token_required
from helpers.swagger.collections import meetup_namespace
from helpers.swagger.models import question_model
from helpers.validators.question import QuestionValidators
from helpers.responses import success_response, error_response
from helpers.vote import get_votes

EXCLUDED_FIELDS = ['deleted', 'deleted_at']


@meetup_namespace.route('/<int:meetup_id>/questions')
class QuestionResource(Resource):
    @token_required
    @meetup_namespace.expect(question_model)
    def post(self, meetup_id):
        """Endpoint to create a question"""
        meetup_schema = MeetupSchema(exclude=EXCLUDED_FIELDS)
        meetup = meetup_schema.dump(
            Meetup.query.filter_by(id=meetup_id, deleted=False).first())

        if not meetup:
            error_response['message'] = 'Meetup not found'
            return error_response, 404

        request_data = request.get_json()
        QuestionValidators.question_validator(request_data)

        request_data.update(
            {
                'user_id': request.decoded_token['user'],
                'meetup_id': meetup_id
            }
        )

        new_question = Question(**request_data)
        new_question.save()
        question_schema = QuestionSchema(exclude=EXCLUDED_FIELDS)
        success_response['message'] = 'Question successfully created'
        success_response['data'] = {
            'question': question_schema.dump(new_question)
        }

        return success_response, 201

    def get(self, meetup_id):
        """Endpoint to get all questions on a meetup"""
        meetup_schema = MeetupSchema(exclude=EXCLUDED_FIELDS)
        meetup = meetup_schema.dump(
            Meetup.query.filter_by(id=meetup_id, deleted=False).first())

        if not meetup:
            error_response['message'] = 'Meetup not found'
            return error_response, 404

        questions_schema = QuestionSchema(many=True, exclude=EXCLUDED_FIELDS)
        questions = questions_schema.dump(
            Question.query.filter(Question.meetup_id == meetup_id, Question.deleted == False))

        # Adding votes to a question
        for question in questions:
            votes = get_votes(question['id'])
            question.update(votes)

        success_response['message'] = 'Questions successfully fetched'
        success_response['data'] = {
            'questions': questions
        }

        return success_response, 200

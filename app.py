from server.instance import application
from config.environment import environment
from helpers.responses import error_response
import resources.user
import resources.meetup
import resources.question
import resources.vote
import resources.rsvp


@application.errorhandler(404)
def page_not_found(e):
    error_response['message'] = 'Undefined route'
    return error_response, 404


if __name__ == '__main__':
    application.run(
        debug=environment['debug'],
        port=environment['port']
    )

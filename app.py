from server.instance import application
from config.environment import environment
import resources.user
import resources.meetup
import resources.question
import resources.vote


if __name__ == '__main__':
    application.run(
        debug=environment['debug'],
        port=environment['port']
    )

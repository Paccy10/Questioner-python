from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server.instance import application
from models.database import db
from models.user import User
from models.meetup import Meetup
from models.question import Question
from models.vote import Vote
from models.rsvp import Rsvp

migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

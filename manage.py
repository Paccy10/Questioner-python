from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server.instance import server
from models.user import User
from models.meetup import Meetup
from models.question import Question
from models.database import db

app = server.app

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from server.instance import application
from config.environment import environment

load_dotenv()


application.config['SQLALCHEMY_DATABASE_URI'] = environment['DATABASE_URI']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database
db = SQLAlchemy(application)

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from server.instance import server
from config.environment import environment

load_dotenv()

app = server.app

app.config['SQLALCHEMY_DATABASE_URI'] = environment['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database
db = SQLAlchemy(app)

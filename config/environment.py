import os, sys
from dotenv import load_dotenv

load_dotenv()

env = 'test' if 'pytest' in sys.modules else os.environ.get('PYTHON_ENV', 'development')

environments = {
    'development': {
        'port': 3000,
        'debug': True,
        'swagger-url': '/api/swagger',
        'DATABASE_URI': os.getenv('DATABASE_URI')
    },
    'test': {
        'port': 3000,
        'debug': False,
        'swagger-url': '/api/swagger',
        'DATABASE_URI': os.getenv('TEST_DATABASE_URI')
    }
}

environment = environments[env]

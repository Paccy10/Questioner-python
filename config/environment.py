import os
import sys
from dotenv import load_dotenv

load_dotenv()

env = 'test' if 'pytest' in sys.modules else os.environ.get(
    'PYTHON_ENV', 'development')

environments = {
    'development': {
        'port': 4000,
        'debug': True,
        'swagger-url': '/documentation',
        'DATABASE_URI': os.getenv('DATABASE_URL')
    },
    'test': {
        'port': 3000,
        'debug': False,
        'swagger-url': '/documentation',
        'DATABASE_URI': os.getenv('TEST_DATABASE_URL')
    }
}

environment = environments[env]

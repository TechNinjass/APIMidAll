import os 
import urllib.parse

DEFAULT_USER = ''
DEFAULT_PWD = ''
DEFAULT_HOST = ''
DEFAULT_PORT = ''

DEFAULT_PWD_ENCODED = urllib.parse.quote_plus(DEFAULT_PWD)

MIDALL_DATABASE = os.environ.get('MIDALL_DATABASE', 'midall')

MIDALL_DB_SCHEMA = f"{MIDALL_DATABASE}.{os.environ.get('MIDALL_DB_SCHEMA', 'dbo')}"


MIDALL_DATABASE_URL = os.environ.get(
    'MIDALL_DATABASE_URL',
    f'mssql+pymssql://{DEFAULT_USER}:{DEFAULT_PWD_ENCODED}@{DEFAULT_HOST}:{DEFAULT_PORT}/{MIDALL_DATABASE}'
)

SQLALCHEMY_TRACK_MODIFICATIONS = int(os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', '0')) == 1
SQLALCHEMY_ECHO = int(os.environ.get('SQLALCHEMY_ECHO', '0')) == 1
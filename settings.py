# settings.py
from os import path, environ
from dotenv import load_dotenv

dot_env_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dot_env_path)

EVERNOTE_API_KEY = environ.get('EVERNOTE_API_KEY')
EVERNOTE_CONSUMER_KEY = environ.get('EVERNOTE_CONSUMER_KEY')
EVERNOTE_CONSUMER_SECRET = environ.get('EVERNOTE_CONSUMER_SECRET')

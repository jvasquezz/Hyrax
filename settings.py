# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dot_env_path = join(dirname(__file__), '.env')
load_dotenv(dot_env_path)

EVERNOTE_API_KEY = os.environ.get('EVERNOTE_API_KEY')
EVERNOTE_CONSUMER_KEY = os.environ.get('EVERNOTE_CONSUMER_KEY')
EVERNOTE_CONSUMER_SECRET = os.environ.get('EVERNOTE_CONSUMER_SECRET')

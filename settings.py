# settings.py
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
import sys

from dotenv import load_dotenv

from os import path, environ


def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by pyInstaller
    return hasattr(sys, "frozen")


def module_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return path.dirname(unicode(sys.executable, encoding))
    return path.dirname(unicode(__file__, encoding))


dot_env_path = path.join(module_path(), '.env')
load_dotenv(dot_env_path)

EVERNOTE_API_KEY = environ.get('EVERNOTE_API_KEY')
EVERNOTE_CONSUMER_KEY = environ.get('EVERNOTE_CONSUMER_KEY')
EVERNOTE_CONSUMER_SECRET = environ.get('EVERNOTE_CONSUMER_SECRET')
APP_VERSION = '0.4.1'

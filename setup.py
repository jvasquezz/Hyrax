# coding=utf-8
"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['app.py']
APP_NAME = 'Hyrax'
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['resources', 'scripts'],
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Cloud connected typesetting",
        'CFBundleIdentifier': "com.rurouni.macOS.hyrax",
        'CFBundleVersion': "0.2.1",
        'CFBundleShortVersionString': "0.2.1",
        'NSHumanReadableCopyright': u"Copyright © 2016, Rurouni, All Rights Reserved"
    }
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

from os import system
with open('requirements.txt') as req:
    for package in req:
        system('pip install ' + package)

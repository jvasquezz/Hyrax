from os import system
with open('requirements.txt') as f:
    for line in f:
        system('pip install ' + line)

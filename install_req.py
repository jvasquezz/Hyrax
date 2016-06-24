import os
with open('requirements.txt') as f:
    for line in f:
        os.system('pip install ' + line)

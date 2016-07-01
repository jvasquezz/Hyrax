### Hyrax rune [![Build Status](https://travis-ci.com/jvasquezz/Hyrax.svg?token=bGrcyjFtugXV4xQLdK6k&branch=develop)](https://travis-ci.com/jvasquezz/Hyrax)
#### Cloud connected typesetting system


##### 1. Standalone installation with PyInstaller

```bash
➜  ~ pip install pyinstaller
➜  ~ pyi-makespec --windowed --onedir --i ./resources/img/icn.icns \
      --osx-bundle-identifier "com.myname.macOS.myappname" app.py
```
Now, modify your `.spec` file:

```python
added_files = [
 ('resources/img', 'resources/img'),
 ( 'README.md', '.' )
 ]
```
initialize a dictionary `added_files` with the relative path to your resources and set `datas = added_files`. In my application I used images located at ./resources/img relative to my main.py file.

And to finilize, this is perhaps the easiest to forget step and not-so obvious:

```bash
➜  ~ pyinstaller --onefile app.spec
```


Refer to this post [here](http://stackoverflow.com/a/38046953/5994618).

##### 2. Standalone with py2app

```javascript
➜ virtualenv venv
➜ source ./venv/bin/activate
(venv) ➜ pip install -U py2app
(venv) ➜ py2applet --make-setup app.py
(venv) ➜ python setup.py py2app -A
```

##### Your output should be similar to this

```bash
# from your root dir
➜ virtualenv venv
    New python executable in ~/PycharmProjects/Hyrax/resources/venv/bin/python
    Installing setuptools, pip, wheel...done.
➜ source ./venv/bin/activate  
(venv) ➜ py2applet --make-setup app.py
    Wrote setup.py
(venv) ➜ python setup.py py2app -A
    running py2app
    creating
    # more stuff...
    *** creating application bundle: app ***
    Done!
```

##### Build for deployment

```bash
➜ rm -rf build dist
➜ python setup.py py2app
```

Include packages in your setup.py `'packages': ['resources', 'scripts']`

Your setup file should look like this:
```python
from setuptools import setup

APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['resources', 'scripts']
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```

##### Known errors related to "py2app" module:

```python
AttributeError: 'ModuleGraph' object has no attribute 'scan_code'
AttributeError: 'ModuleGraph' object has no attribute 'load_module'
```

Edit file where error occurred and rename `scan_code` or `load_module` with underscore on front i.e. `_load_module`. For more details, refer to [From a Python script to a portable Mac application with py2app](http://www.marinamele.com/from-a-python-script-to-a-portable-mac-application-with-py2app)

##### 3. Configure jenkins with Github private repositories
```bash
➜  ~ sudo su - jenkins
macbookPro:~ jenkins$
macbookPro:~ jenkins$ git clone git@github.com:jvasquezz/privaterepo.git
```

#####  4. Add an Info.plist to the bundle:

Using PyInstaller, add this dictionary to the app BUNDLE:

```
info_plist={
            'NSHighResolutionCapable': 'True',
            'CFBundleName': APP_NAME,
            'CFBundleDisplayName': APP_NAME,
            'CFBundleGetInfoString': "Cloud connected typesetting",
            'CFBundleIdentifier': "com.rurouni.macOS.hyrax",
            'CFBundleVersion': "0.3.0",
            'CFBundleShortVersionString': "0.3.0",
            'NSHumanReadableCopyright': "Copyright © 2016, Rurouni, All Rights Reserved"
            }
```

And for py2app, add to the setup file as OPTIONS:
```
    'plist': {
        ...
```

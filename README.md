<h3> Hyrax rune </h3> 
<h4> Cloud connected typesetting system </h4>

<h5>Get it running:</h5>

```javascript
$ virtualenv venv
$ source ./venv/bin/activate
(venv) $ pip install -U py2app
(venv) $ py2applet --make-setup app.py
(venv) $ python setup.py py2app -A 
```

<h5>Your output should be similar to this</h5>

```javascript
# from your root dir
$ virtualenv venv
    New python executable in ~/PycharmProjects/Hyrax/resources/venv/bin/python
    Installing setuptools, pip, wheel...done.
$ source ./venv/bin/activate  
(venv) $ py2applet --make-setup app.py
    Wrote setup.py
(venv) $ python setup.py py2app -A
    running py2app
    creating /Users/username/Hyrax/build/bdist.macosx-10.11-intel/pythonX.Y-semi_standalone/app
    creating /Users/username/Hyrax/build/bdist.macosx-10.11-intel/pythonX.Y-semi_standalone/app/collect
    creating /Users/username/Hyrax/build/bdist.macosx-10.11-intel/pythonX.Y-semi_standalone/app/temp
    creating build/bdist.macosx-10.11-intel/python2.7-semi_standalone/app/lib-dynload
    creating build/bdist.macosx-10.11-intel/python2.7-semi_standalone/app/Frameworks
    *** creating application bundle: app ***
    Done!
```

<h5>Build for deployment<h5>
```javascript
$ rm -rf build dist
$ python setup.py py2app

```

Flask WebApp Boilerplate Project
=========================
http://flask.pocoo.org/

This is a skeleton project meant to be helpful for those who want to quickly jump into a new flask project. UserAccounts, Tests, Caching, Mail, User Registration, Roles, Python Script Commands, and Twitter Bootstrap are already configured.

The Flask Boilerplate Project consists of many projects merged into one to provide the most flexible boilerplate for your flask project.

It is pre-configured for a production Heroku environment, but can be adjusted to suit your needs.

If you would like other confirgurations available or to add certain features, create an issue and I will do my best.


Installation
------------
1. Download via git:

        git clone git://github.com/hansonkd/FlaskBootstrapSecurity.git

2. Change into the cloned directory

        cd FlaskBootstrapSecurity

2. Get VirtualEnv and VirtualEnvWrapper set up. See here for further details: http://www.doughellmann.com/docs/virtualenvwrapper/
	
3. Create a virtualenvironment

        mkvirtualenv environment

4. Install the required python dependancies:

        pip install -r requirements.txt
    
5. Edit `flask_application/config.py` to change your mail server, password salt and other settings:

        class Config(object):
            SECRET_KEY = '{SECRET_KEY}'
            SITE_NAME = 'Flask Site'
            SITE_ROOT_URL = 'http://example.com'
            LOG_LEVEL = logging.DEBUG

            MEMCACHED_SERVERS = ['localhost:11211']
            SYS_ADMINS = ['foo@example.com']

            # Mongodb support
            MONGODB_DB = 'testing'
            MONGODB_HOST = 'localhost'
            MONGODB_PORT = 27017

            # Configured for Gmail
            DEFAULT_MAIL_SENDER = 'Admin < username@example.com >'
            MAIL_SERVER = 'smtp.gmail.com'
            MAIL_PORT = 465
            MAIL_USE_SSL = True
            MAIL_USERNAME = 'username@gmail.com'
            MAIL_PASSWORD = '*********'

            # Flask-Security setup
            SECURITY_EMAIL_SENDER = 'Security < security@example.com >'
            SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
            SECURITY_REGISTERABLE = True
            SECURITY_RECOVERABLE = True
            SECURITY_URL_PREFIX = '/auth'
            SECUIRTY_POST_LOGIN = '/'
            SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
            # import uuid; salt = uuid.uuid4().hex
            SECURITY_PASSWORD_SALT = '2b8b74efc58e489e879810905b6b6d4dc6'

            # CACHE
            CACHE_TYPE = 'simple'


7. Run a development server:
        
        python manage.py runserver

Usage
-----

##Commands
_Run these commands by using `python manage.py <command>`_


* `reset_db` - Drops all Mongo documents
* `populate_db` - Script to fill the database with new data (either for testing or for initial). You can edit the `populate_data` command in `flask_application/script.py` (Right now it is set up to add Users.)
* `runserver` - Runs a debug server
* `clean` - Removes *.pyc files
* `shell` - Opens a shell within the Flask context
* `show_urls` - Lists the urls that are available
* `run_tests` - Runs unittests using nose.
* Commands included with Flask-Security can be found here: http://packages.python.org/Flask-Security/#flask-script-commands and by looking in `flask_application/script.py`

##Templates
The base template used Flask-Bootstrap for basic templates. This project can be overridden by adding your own templates to the `templates` folder or by taking it out.

##Structure
The structure provides you with a way to scale your app comfortably. All sub-apps have their own directory (the skeleton apps `admin/`, `public/`, `users/` are provided) and all views inherit from one common view class. Class-based views give you the ability to subclass and inherit many features. If extra-functionality is needed for your views, you can quickly edit the baseclass and be done with it.

The same carries over to your models. It is preferable to subclass `FlaskDocument` than to subclass mongoengines `Document` directly. Because `FlaskDocument` is under your control, you can override and add functions to enrich your all your models at once.

##Running Tests
You can run the unittests either with `ENVIRONMENT=TESTING ./manage.py run_tests`, with `ENVIRONMENT=TESTING . /bin/run_tests.sh` or `ENVIRONMENT=TESTING nosetests`.

This repo is configured for Continuous Integration with Travis. Every commit runs the test suite. You can add Travis to your own projects by pointing it at your forked repository.

##Static Content
This project is designed to use CSSMin and Flask-Assets to manage Assets to save on bandwidth and requests. 

You can find this in the `style` block of the layout template. You can also simply edit `static/css/site.css` as that is included in the base setup.

Deploying
---------

This app is all ready configured to be deployed on Heroku with MongoHQ (database) and Mandrill (email).

Simply add the free tiers of those services, change your `config.py` `SERVER_NAME`, set the production config with `heroku config:set ENVIRONMENT=PRODUCTION` and deploy normally.


Credit
------
####Required Python Projects:

* unittest2
* Flask
* Flask-Assets
* cssmin
* Flask-WTF
* Flask-Script
* Flask-Mail
* Flask-Cache
* Flask-Security
* Flask-MongoEngine
* Flask-Testing
* python-memcached

####Non-Python Projects:
* Twitter Bootstrap

####Contributing Projects:
* Flask-Security Example App
* https://github.com/mbr/flask-bootstrap

LICENSE &amp; COPYRIGHT
-----------------------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

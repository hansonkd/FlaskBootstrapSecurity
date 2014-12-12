import logging
import os
from pymongo.uri_parser import parse_uri


class Config(object):
    def __init__(self):
        self.DEBUG = False
        self.TESTING = False
        self.HEROKU = False
        self.PRODUCTION = False

        self.SECRET_KEY = '{SECRET_KEY}'
        self.SITE_NAME = 'Flask Site'
        self.LOG_LEVEL = logging.DEBUG
        
        # Look at Flask's documentation on SERVER_NAME to correctly configure,
        # or you might end up with 404s.
        self.SERVER_NAME = 'flaskbootstrapsecurity-hansonkd.c9.io'

        self.SYS_ADMINS = ['foo@example.com']

        # SQLAlchemy support
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

        # Configured for Gmail
        self.DEFAULT_MAIL_SENDER = 'Admin < username@example.com >'
        self.MAIL_SERVER = 'smtp.gmail.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = 'user@example.com'
        self.MAIL_PASSWORD = '****************'

        # Flask-Security setup
        self.SECURITY_EMAIL_SENDER = 'Security < security@example.com >'
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
        self.SECURITY_REGISTERABLE = True
        self.SECURITY_RECOVERABLE = True
        self.SECURITY_URL_PREFIX = '/auth'
        self.SECUIRTY_POST_LOGIN = '/'
        self.SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
        # import uuid; salt = uuid.uuid4().hex
        self.SECURITY_PASSWORD_SALT = '2b8b74efc58e489e879810905b6b6d4dc6'

        self.SECURITY_CONFIRMABLE = True
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

        # CACHE
        self.CACHE_TYPE = 'simple'


class ProductionConfig(Config):
    def __init__(self):
        super(ProductionConfig, self).__init__()
        self.ENVIRONMENT = 'Production'
        self.HEROKU = True
        self.PRODUCTION = True
        self.LOG_LEVEL = logging.INFO
        self.SERVER_NAME = 'example.com'

        self.MAIL_SERVER = 'smtp.mandrillapp.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = os.getenv('MANDRILL_USERNAME')
        self.MAIL_PASSWORD = os.getenv('MANDRILL_APIKEY')

        self.SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    '''
    Use "if app.debug" anywhere in your code,
    that code will run in development mode.
    '''
    def __init__(self):
        super(DevelopmentConfig, self).__init__()
        self.ENVIRONMENT = 'Dev'
        self.DEBUG = True
        self.TESTING = False


class TestingConfig(Config):
    '''
    A Config to use when we are running tests.
    '''
    def __init__(self):
        super(TestingConfig, self).__init__()
        self.ENVIRONMENT = 'Testing'
        self.DEBUG = False
        self.TESTING = True

        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


environment = os.getenv('ENVIRONMENT', 'DEVELELOPMENT').lower()
# Alternatively this may be easier if you are managing multiple aws servers:
# environment = socket.gethostname().lower()

if environment == 'testing':
    app_config = TestingConfig()
elif environment == 'production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()

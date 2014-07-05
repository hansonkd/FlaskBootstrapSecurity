import logging
import os
from pymongo.uri_parser import parse_uri


class Config(object):
    def __init__(self):
        self.SECRET_KEY = '{SECRET_KEY}'
        self.SITE_NAME = 'Flask Site'
        self.LOG_LEVEL = logging.DEBUG
        self.SERVER_NAME = 'localhost:5000'

        self.SYS_ADMINS = ['foo@example.com']

        # Mongodb support
        self.MONGODB_SETTINGS = self.mongo_from_uri(
            'mongodb://localhost:27017/testing'
        )

        # Configured for Gmail
        self.DEFAULT_MAIL_SENDER = 'Admin < username@example.com >'
        self.MAIL_SERVER = 'smtp.gmail.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = 'username@gmail.com'
        self.MAIL_PASSWORD = '*********'

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

        # CACHE
        self.CACHE_TYPE = 'simple'

    @staticmethod
    def mongo_from_uri(uri):
        config = parse_uri(uri)
        conn_settings = {
            'db': config['database'],
            'username': config['username'],
            'password': config['password'],
            'host': config['nodelist'][0][0],
            'port': config['nodelist'][0][1]
        }
        return conn_settings


class ProductionConfig(Config):
    def __init__(self):
        super(ProductionConfig, self).__init__()
        self.ENVIRONMENT = 'Production'
        self.DEBUG = False
        self.TESTING = False
        self.LOG_LEVEL = logging.INFO
        self.SERVER_NAME = 'http://example.com'

        self.MAIL_SERVER = 'smtp.mandrillapp.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = 'mandrilluser'
        self.MAIL_PASSWORD = '*********'

        self.SECURITY_CONFIRMABLE = True
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

        self.CACHE_TYPE = 'memcached'
        self.CACHE_MEMCACHED_SERVERS = ['localhost:11211']

        self.MONGODB_SETTINGS = self.mongo_from_uri(os.getenv('MONGOHQ_URL'))


class TestConfig(Config):
    def __init__(self):
        super(TestConfig, self).__init__()
        self.ENVIRONMENT = 'Test'
        self.DEBUG = False
        self.TESTING = True


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


if os.getenv('TEST') == 'yes':
    app_config = TestConfig()
elif os.getenv('PRODUCTION') == 'yes':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()

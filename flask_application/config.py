import logging


class Config(object):
    SECRET_KEY = '{SECRET_KEY}'
    SITE_NAME = 'Flask Site'
    LOG_LEVEL = logging.DEBUG
    SERVER_NAME = 'localhost:5000'

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


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = logging.INFO
    SERVER_NAME = 'http://example.com'

    MAIL_SERVER = 'smtp.mandrillapp.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'mandrilluser'
    MAIL_PASSWORD = '*********'

    SECURITY_CONFIRMABLE = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

    CACHE_TYPE = 'memcached'
    CACHE_MEMCACHED_SERVERS = ['localhost:11211']

    MONGO_DB = 'production'


class TestConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    DEBUG = False
    TESTING = True


class DevelopmentConfig(Config):
    '''
    Use "if app.debug" anywhere in your code,
    that code will run in development mode.
    '''
    SITE_ROOT_URL = 'http://localhost:5000'
    DEBUG = True
    TESTING = False

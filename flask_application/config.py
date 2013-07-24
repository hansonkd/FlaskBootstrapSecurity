class Config(object):
    SECRET_KEY = '{SECRET_KEY}'
    SITE_NAME = 'Flask Site'
    SITE_ROOT_URL = 'http://example.com'
    MEMCACHED_SERVERS = ['localhost:11211']
    SYS_ADMINS = ['foo@example.com']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


    #configured for GMAIL
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'username@gmail.com'
    MAIL_PASSWORD = '*********'
    DEFAULT_MAIL_SENDER = 'Admin < username@gmail.com >'
    
    #SECURITY_CONFIRMABLE = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_URL_PREFIX = "/auth"

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECURITY_CONFIRMABLE = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

class TestConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    DEBUG = False
    TESTING = True

class DevelopmentConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    '''Use "if app.debug" anywhere in your code, that code will run in development code.'''
    #DEBUG = True
    #TESTING = True


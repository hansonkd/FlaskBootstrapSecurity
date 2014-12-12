from flask import current_app

from flask.ext.testing import TestCase

from flask_application import app
from flask_application.script import ResetDB, PopulateDB


class FlaskTest(TestCase):
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    TESTING = True

    def create_app(self):
        return app

    def setUp(self):
        self.assertTrue(
            current_app.config['TESTING'],
            'Testing is not set. Are you sure you are using the right config?'
        )
        current_app.config['WTF_CSRF_ENABLED'] = False
        current_app.db.drop_all()
        current_app.db.create_all()
        
        PopulateDB.create_roles()
        PopulateDB.create_users()
        self.client = self.app.test_client()

    def tearDown(self):
        current_app.db.session.remove()
        current_app.db.drop_all()

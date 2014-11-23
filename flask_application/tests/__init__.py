from flask import current_app

from flask.ext.testing import TestCase

from flask_application import app
from flask_application.script import ResetDB, PopulateDB


class FlaskTest(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        self.assertTrue(
            current_app.config['TESTING'],
            'Testing is not set. Are you sure you are using the right config?'
        )
        current_app.config['WTF_CSRF_ENABLED'] = False
        ResetDB.drop_collections()
        PopulateDB.create_roles()
        PopulateDB.create_users()
        self.client = self.app.test_client()

    def tearDown(self):
        ResetDB.drop_collections()

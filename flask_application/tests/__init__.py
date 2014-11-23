from flask_application import app
from flask_application.script import ResetDB, PopulateDB
import unittest


class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.assertTrue(
            app.config['TESTING'],
            'Testing is not set. Are you sure you are using the right config?'
        )
        app.config['WTF_CSRF_ENABLED'] = False
        ResetDB().run()
        PopulateDB().run()
        self.app = app
        self.client = app.test_client()

    def tearDown(self):
        ResetDB().run()

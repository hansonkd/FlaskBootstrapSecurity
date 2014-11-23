from flask.ext.script import Command
from flask_application.models import FlaskDocument
from flask_application.users.populate import populate_data


class ResetDB(Command):
    """Drops all tables and recreates them"""
    def run(self, **kwargs):
        for klass in FlaskDocument.all_subclasses():
            klass.drop_collection()


class PopulateDB(Command):
    """Fills in predefined data into DB"""
    def run(self, **kwargs):
        populate_data()

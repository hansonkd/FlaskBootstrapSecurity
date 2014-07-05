from flask.ext.script import Command
from flask_application.populate import populate_data
from flask_application.models import User, Role


class ResetDB(Command):
    """Drops all tables and recreates them"""
    def run(self, **kwargs):
        for m in [User, Role]:
            m.drop_collection()


class PopulateDB(Command):
    """Fills in predefined data into DB"""
    def run(self, **kwargs):
        populate_data()

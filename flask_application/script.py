from flask import current_app

from flask.ext.script import Command
from flask.ext.security.confirmable import confirm_user

from flask_application import app


class ResetDB(Command):
    """Drops all tables and recreates them"""
    def run(self, **kwargs):
        self.drop_tables()

    @staticmethod
    def drop_tables():
        current_app.db.drop_all()


class PopulateDB(Command):
    """Fills in predefined data to DB"""
    def run(self, **kwargs):
        self.create_roles()
        self.create_users()

    @staticmethod
    def create_roles():
        for role in ('admin', 'editor', 'author'):
            current_app.user_datastore.create_role(name=role, description=role)
        current_app.user_datastore.commit()

    @staticmethod
    def create_users():
        for u in (('matt@lp.com', 'password', ['admin'], True),
                  ('joe@lp.com', 'password', ['editor'], True),
                  ('jill@lp.com', 'password', ['author'], True),
                  ('tiya@lp.com', 'password', [], False)):
            user = current_app.user_datastore.create_user(
                email=u[0],
                password=u[1],
                roles=u[2],
                active=u[3]
            )
            confirm_user(user)

            current_app.user_datastore.commit()

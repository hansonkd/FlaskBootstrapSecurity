from flask_application import user_datastore, app
from flask_application.models import db


def create_roles():
    for role in ('admin', 'editor', 'author'):
        user_datastore.create_role(name=role, description=role)
    user_datastore.commit()
        
def create_users():
    for u in  (('matt','matt@lp.com','password',['admin'],True),
               ('joe','joe@lp.com','password',['editor'],True),
               ('jill','jill@lp.com','password',['author'],True),
               ('tiya','tiya@lp.com','password',[],False)):
        user_datastore.create_user(username=u[0], email=u[1], password=u[2],
                                   roles=u[3], active=u[4])
        user_datastore.commit()

def populate_data():
	create_roles()
	create_users()
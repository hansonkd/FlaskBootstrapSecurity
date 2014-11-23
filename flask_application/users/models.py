from flask.ext.security import UserMixin, RoleMixin

from flask_application.models import db, FlaskDocument


class Role(FlaskDocument, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(FlaskDocument, UserMixin):
    email = db.StringField(max_length=255)
    username = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

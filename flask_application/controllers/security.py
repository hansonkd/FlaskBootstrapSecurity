#!/usr/bin/env python

import datetime

from flask import Blueprint, render_template, request, url_for, redirect, flash, abort

from flask.ext.security import (User, Security, LoginForm, user_datastore, current_user,
                                login_required, roles_required, roles_accepted)

from flask.ext.security.datastore.sqlalchemy import SQLAlchemyUserDatastore

from flask_application.helpers import encode_id, decode_id, get_or_abort

from flask_application.models import *
from flask_application import mail

security = Blueprint('security', __name__, url_prefix='/auth')

from flaskext.wtf import Form, TextField, PasswordField, SubmitField, Required, Email, EqualTo, BooleanField, ValidationError


class UserExistValidator(object):
    def __init__(self, field_type="username", message=None):
        self.field_type = field_type
        if not message:
            message = u'Username already Exists'
        self.message = message

    def __call__(self, form, field):
        kw = {
            self.field_type: field.data,
        }
        if db.session.query(User).filter_by(**kw).count():
            raise ValidationError(self.message)

class RegistrationForm(Form):

    username = TextField("Username", 
        validators=[UserExistValidator(), Required(message="Username not provided")])
    email = TextField("Email Address", 
        validators=[Required(message="Username not provided"), Email(message="Invalid Email"), UserExistValidator("email", "Email address already has an account.")])
    password = PasswordField('New Password', 
        validators=[Required(message="Password not provided"), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password', validators=[Required(message="Password not provided")])

    agree = BooleanField('Do you agree to ToS?', validators = [Required(message="You must agree to use this service")])

    submit = SubmitField("Register")


class RegistrationKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    def __init__(self, user_id):
        self.user_id= user_id
        self.created = datetime.datetime.now()

    def __repr__(self):
        return '<RegistrationKey %r>' % self.user_id


@security.route('/')
def index():
        return redirect(url_for("security.login"))

@security.route('/login')
def login():
    return render_template('security/login.html', content='Login Page', action=url_for('auth.authenticate'), form=LoginForm())

@security.route('/profile')
@login_required
def profile():
    flash("testFlash")
    return render_template('security/index.html', content='Profile Page')

@security.route('/post_login')
@login_required
def post_login():
    return render_template('security/index.html', content='Post Login')

@security.route('/post_logout')
def post_logout():
    return render_template('security/index.html', content='Post Logout')

@security.route('/admin')
@roles_required('admin')
def admin():
    return render_template('security/index.html', content='Admin Page')

@security.route('/admin_or_editor')
@roles_accepted('admin', 'editor')
def admin_or_editor():
    return render_template('security/index.html', content='Admin or Editor Page')

@security.route('/register', methods=("GET", "POST"))
def register():
    form=RegistrationForm()
    if form.validate_on_submit():

        user = user_datastore.create_user(username=form.username.data, email=form.email.data, password=form.password.data,
                                   roles=[], active=False)

        activation_key = RegistrationKey(user_id = user.get_id())
        db.session.add(activation_key)
        db.session.commit()

        encoded_id = encode_id(activation_key.id)

        activate_url = app.config.get('SITE_ROOT_URL') + url_for('security.activate', activationid = encoded_id)

        mail.send_message(recipients=[form.email.data],
                      html=render_template('email/registration.html', activate_url = activate_url, user=user),
                      subject="Registration information for %s" % app.config.get('SITE_NAME'))
        flash("Please check your email, %s for activation instructions" % form.email.data)

        return redirect(url_for('security.profile'))

    return render_template('security/login.html', content='Registration', form=form, action=url_for('security.register'))


@security.route('/activate/<activationid>')
def activate(activationid):
    key = get_or_abort(RegistrationKey, decode_id(activationid))
    user = user_datastore.with_id(key.user_id)
    active_user = user_datastore.activate_user(user.email)
    db.session.delete(key)
    db.session.commit()
    flash("Your account has been activated")
    return redirect(url_for('security.login'))
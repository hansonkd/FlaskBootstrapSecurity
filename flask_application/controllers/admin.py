#!/usr/bin/env python

import datetime

from flask import Blueprint, render_template, request, url_for, redirect, flash, abort

from flask.ext.security import (LoginForm, current_user,
                                login_required, roles_required, roles_accepted, SQLAlchemyUserDatastore)

from flask_application.helpers import encode_id, decode_id, get_or_abort

from flask_application.models import *
from flask_application import mail, user_datastore

admin = Blueprint('admin', __name__, url_prefix='/admin')

from flask.ext.wtf import Form, TextField, PasswordField, SubmitField, Required, Email, EqualTo, BooleanField, ValidationError

@admin.route('/admin')
@roles_required('admin')
def admin_page():
    return render_template('security/index.html', content='Admin Page')

@admin.route('/admin_or_editor')
@roles_accepted('admin', 'editor')
def admin_or_editor():
    return render_template('security/index.html', content='Admin or Editor Page')
    
@admin.route('/profile')
@login_required
def profile():
    flash("testFlash")
    return render_template('security/index.html', content='Profile Page')
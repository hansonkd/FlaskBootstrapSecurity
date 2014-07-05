#!/usr/bin/env python

import datetime

from flask import Blueprint, render_template
from flask_application import app
from flask.ext.security import login_required

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template(
        'home/index.html',
                config=app.config,
                now=datetime.datetime.now,
            )

@frontend.route('/profile')
@login_required
def profile():
    return render_template(
        'profiles/profile.html',
        content='Profile Page')
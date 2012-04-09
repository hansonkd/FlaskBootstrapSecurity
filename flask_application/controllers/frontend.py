#!/usr/bin/env python

import datetime

from flask import Blueprint, render_template
from flask_application import app

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template(
                'index.html',
                config=app.config,
                now=datetime.datetime.now,
            )
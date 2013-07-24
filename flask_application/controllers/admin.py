from flask import Blueprint, render_template
from flask.ext.security import (login_required, roles_required, roles_accepted)
from flask_application.helpers import encode_id, decode_id, get_or_abort
from flask_application.models import *

admin = Blueprint('admin', __name__, url_prefix='/admin')

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
    flash('testFlash')
    return render_template('security/index.html', content='Profile Page')
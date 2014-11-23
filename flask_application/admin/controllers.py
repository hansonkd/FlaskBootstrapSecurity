from flask import Blueprint
from flask.ext.security import roles_required, roles_accepted

from flask_application.controllers import TemplateView

admin = Blueprint('admin', __name__, url_prefix='/admin')


class AdminView(TemplateView):
    blueprint = admin
    route = '/'
    route_name = 'index'
    template_name = 'admin/index.html'
    decorators = [roles_required('admin')]

    def get_context_data(self, *args, **kwargs):
        return {
            'content': 'This is the Admin Page'
        }


class AdminOrEditorView(TemplateView):
    blueprint = admin
    route = '/admin/editor'
    route_name = 'admin_or_editor'
    template_name = 'admin/index.html'
    decorators = [roles_accepted('admin', 'editor')]

    def get_context_data(self, *args, **kwargs):
        return {
            'content': 'This is the Admin/Editor Page'
        }

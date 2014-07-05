from flask import Blueprint
from flask.ext.security import roles_required

from flask_application.controllers import TemplateView

admin = Blueprint('admin', __name__, url_prefix='/admin')


class AdminView(TemplateView):
    route = '/admin'
    template_name = 'security/index.html'
    decorators = [roles_required('admin')]

    def get_context_data(self, *args, **kwargs):
        return {
            'content': 'This is the Admin Page'
        }

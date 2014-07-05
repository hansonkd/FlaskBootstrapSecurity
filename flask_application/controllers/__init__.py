# http://flask.pocoo.org/docs/patterns/packages/

from flask.views import MethodView, MethodViewType
from flask import render_template
from flask._compat import with_metaclass

from flask_application import app


class ViewMeta(MethodViewType):
    def __init__(cls, name, bases, dct):
        super(ViewMeta, cls).__init__(name, bases, dct)

        route = dct.get('route')
        if route and route != NotImplemented:
            endpoint = dct.get('route_name', name.rstrip('View').lower())
            app.add_url_rule(route, view_func=cls().as_view(endpoint))


class BaseView(with_metaclass(ViewMeta, MethodView)):
    route = NotImplemented


class TemplateView(BaseView):
    template_name = NotImplemented

    def get_context_data(self, *args, **kwargs):
        return {}

    def get_template(self, *args, **kwargs):
        return self.template_name

    def process(self, *args, **kwargs):
        return render_template(self.get_template(*args, **kwargs),
                               **self.get_context_data(*args, **kwargs))

    def get(self, *args, **kwargs):
        return self.process(*args, **kwargs)

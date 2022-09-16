from types import SimpleNamespace as SN
from flask import current_app, abort, request
from flask.views import MethodView


class BaseView(MethodView):
    def __init__(self):
        self.app = current_app
        self.context = SN()
        self.context.paginate = SN()

from .home import home as home_blueprint
from .home.views import Home


class Route:
    @staticmethod
    def init_app(app):
        home_blueprint.add_url_rule('/', view_func=Home.as_view('home'))

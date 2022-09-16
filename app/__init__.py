from flask import Flask
from flask import send_from_directory, request
from .errors import page_forbidden, page_not_found, internal_server_error, method_not_allowed
from .routes import Route


def create_app(config_name):
    app = Flask(__name__)

    app.register_error_handler(403, page_forbidden)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, internal_server_error)

    @app.route('/robots.txt')
    @app.route('/sitemap.xml')
    def static_from_root():
        return send_from_directory(app.static_folder, request.path[1:])

    Route.init_app(app)
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
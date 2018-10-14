""" App module to bring together the whole app."""
from flask import Flask
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

    from .api.v1.routes import v_1 as v1
    app.register_blueprint(v1)

    return app

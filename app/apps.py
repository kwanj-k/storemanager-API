""" App module to bring together the whole app."""
from datetime import timedelta


from flask import Flask
from flask_jwt_extended import JWTManager


from instance.config import app_config

jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False
    #TODO change and hide the secret key
    app.config['JWT_SECRET_KEY'] = 'super-secret-key-that'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=72)
    jwt.init_app(app)

    from .api.v1.routes import v_1 as v1
    app.register_blueprint(v1)

    return app

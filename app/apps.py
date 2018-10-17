""" App module to bring together the whole app."""
from datetime import timedelta


from flask import Flask,jsonify
from flask_jwt_extended import JWTManager


from instance.config import app_config

jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False
    # TODO change and hide the secret key
    app.config['JWT_SECRET_KEY'] = 'e9i%i6o%)pu05m7&&2)mvwt7q!7lj_r+q@pbi5#0835g3&@=a1'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=72)
    

    jwt.init_app(app)
    

    from .api.v1.routes import v_1 as v1
    from .api.v1.routes import v1 as jwtapi
    app.register_blueprint(v1)
    jwt._set_error_handler_callbacks(jwtapi)

    return app

import importlib

from flask import Flask

from .config import Config


def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_filename)
    for installed_app in app.config['REGISTERED_APP']:
        view = importlib.import_module('views.{}'.format(installed_app))
        app.register_blueprint(view.blueprint)

    return app


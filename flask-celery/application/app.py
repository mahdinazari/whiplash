import importlib

from flask import Flask

from .config import Config


installed_app = Config.REGISTERED_APP


def create_app(config_filename):
    """
    Construct the core application.
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_filename)

    for installed_app in app.config['REGISTERED_APP']:
        view = importlib.import_module('views.{}'.format(installed_app))
        app.register_blueprint(view.blueprint)

    return app


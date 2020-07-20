import os

from flask import Flask

from serve.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('serve')

    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errorhandlers(app)
    register_shell_context(app)
    register_template_context(app)
    return app


def register_extensions(app):
    pass


def register_blueprints(app):
    pass


def register_shell_context(app):
    pass


def register_template_context(app):
    pass


def register_errorhandlers(app):
    pass


def register_commands(app):
    pass

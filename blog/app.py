from flask import Flask

from blog.extensions import configuration


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    return app

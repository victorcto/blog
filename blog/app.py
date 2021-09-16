from flask import Flask

from blog.extensions import config, toolbar, web


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    web.init_app(app)
    return app

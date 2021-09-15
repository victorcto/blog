from flask import Flask

from blog.web.main import bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app

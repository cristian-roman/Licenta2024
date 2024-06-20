from flask import Flask
from flask_cors import CORS

from app_init.init import register_dependencies


def create_app():
    app = Flask(__name__)

    register_dependencies(app)

    CORS(app)
    return app


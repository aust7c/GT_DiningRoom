from config import config
from flask import Blueprint
from flask import Flask
from flask import current_app
from flask_pymongo import PyMongo


mongo = PyMongo()




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mongo.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
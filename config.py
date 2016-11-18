from flask import Flask
from flask_pymongo import PyMongo
import os
DEBUG = True

class Config:
    MONGO_DBNAME = 'geetest_dining'
    MONGO_URI = 'mongodb://diningroom:dining08room@ds155727.mlab.com:55727/geetest_dining'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'default': DevelopmentConfig
}

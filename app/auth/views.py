from flask import render_template
from . import auth
from app import mongo


@auth.route('/')
def index():
    return 'this is index page'


@auth.route('/login')
def login():
    return "hello"

@auth.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name':'austin180012'})
    return  'Yeah!!! You Add The Data To MongoDB Successful!'


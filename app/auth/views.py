from flask import render_template , Flask,url_for,request,session,redirect
from . import auth
from app import mongo
import bcrypt

@auth.route('/')
def index():
    if 'username' in session:
        return 'Congratulations! You are logged in as' + session['username']
    return render_template('auth/index.html')

@auth.route('/login',methods=['POST','GET'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name':request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('auth.index'))

    return 'Invalid username/password combination'

@auth.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'name':request.form['username'],'password':hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('auth.index'))

        return 'This Username already exists!'
    return render_template('auth/register.html')

# @auth.route('/add')
# def add():
#     user = mongo.db.users
#     user.insert({'name':'austin180012'})
#     return  'Yeah!!! You Add The Data To MongoDB Successful!'
#

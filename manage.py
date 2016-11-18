from flask_script import Manager
from flask import Flask
# from app import app
from app import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# app = Flask(__name__)


manager = Manager(app)

if __name__ == "__main__":
    manager.run()
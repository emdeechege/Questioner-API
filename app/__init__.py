'''Creating app'''
import os
from flask import Flask
from instance.config import app_config
"""importing the configurations from the .config file which is in the instance folder"""


def create_app():
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__)

    # Creating the app configurations
    # app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    return app

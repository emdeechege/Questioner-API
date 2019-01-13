'''Creating app'''
import os
from flask import Flask
from .api.v1.views.meetup_views import v1_meetup_blueprint
from .api.v1.views.questions_views import v1_question_blueprint
from .api.v1.views.auth_views import v1_auth_blueprint
# from instance.config import app_config
# """importing the configurations from the .config file which is in the instance folder"""


def create_app():
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__)
    # register blueprints
    app.register_blueprint(v1_meetup_blueprint)
    app.register_blueprint(v1_question_blueprint)
    app.register_blueprint(v1_auth_blueprint)
    # Creating the app configurations
    # app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    return app

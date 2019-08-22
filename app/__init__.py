"""Creating app"""
import os
from flask import Flask
from instance import config
from app.connect import QuestionerDB


from .api.v1.views.meetup_views import v1_meetup_blueprint
from .api.v1.views.questions_views import v1_question_blueprint
from .api.v1.views.auth_views import v1_auth_blueprint
from .api.v2.views.auth_views import v2_auth
from .api.v2.views.meetup_views import v2_meetup
from .api.v2.views.questions_views import v2_question


def create_app(config):
    """creating  the app using the configurations in the dictionary created in the .config file"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    QuestionerDB.init_db(app.config["DATABASE_URL"])
    QuestionerDB.create_tables()


    """register v1 blueprints"""
    app.register_blueprint(v1_meetup_blueprint)
    app.register_blueprint(v1_question_blueprint)
    app.register_blueprint(v1_auth_blueprint)

    app.register_blueprint(v2_auth)
    app.register_blueprint(v2_meetup)
    app.register_blueprint(v2_question)


    # import pdb; pdb.set_trace()


    return app

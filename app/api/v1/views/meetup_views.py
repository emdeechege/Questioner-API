from flask import Flask, Blueprint, request, jsonify, make_response
from models import meetup_models
from datetime import datetime

v1_meetup_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')
meetups = meetup_models.MeetupModels()


@v1_meetup_blueprint.route('/create_meetup', methods=['POST'])
def create_meetup():
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})
    meetup_id = len(meetups.all_meetups)+1
    title = data.get('title')
    organizer = data.get('organizer')
    location = data.get('location')
    created_on = data.get('created_on')
    happeningOn = data.get('happeningOn')
    tags = data.get('tags')

    meet = jsonify(meetups.create_meetup(meetup_id, title, organizer,
                                         location, created_on, happeningOn, tags))
    meet.status_code = 201
    return meet

from flask import jsonify, Blueprint, request, json, make_response
from datetime import datetime
from ..models.meetups_models import Meetup, Rsvp


v2_meetup = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetups = Meetup()
rsvp = Rsvp()


@v2_meetup.route('/meetups', methods=['POST'])
def create_meetup():
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})

    if not all(field in data for field in ["title", "organizer",\
     "images", "location", "happening_on", "tags"]):
        return jsonify({"status": 400,\
         "message": "Please fill in all the required input fields"}), 400


    title = data.get('title')
    created_on = data.get('time')
    organizer = data.get('organizer')
    images = data.get("images")
    location = data.get('location')
    happening_on = data.get('happening_on')
    tags = data.get('tags')

    meet = jsonify(meetups.create_meetup(title, created_on,\
     organizer, images, location, happening_on, tags))
    meet.status_code = 201

    return jsonify(meet, {
        "status": 201,
        "message": "Meetup added successfuly"
    }), 201

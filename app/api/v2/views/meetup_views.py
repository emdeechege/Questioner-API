from flask import jsonify, Blueprint, request, json, make_response
from datetime import datetime
from ..models.meetups_models import Meetup


v2_meetup = Blueprint('meetup', __name__, url_prefix='/api/v2')

MEETUPS = Meetup()



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
    organizer = data.get('organizer')
    images = data.get("images")
    location = data.get('location')
    happening_on = data.get('happening_on')
    tags = data.get('tags')

    meet = MEETUPS.create_meetup(title,\
     organizer, images, location, happening_on, tags)
    return jsonify(meet, {
        "status": 201,
        "message": "Meetup added successfuly"
    }), 201

@v2_meetup.route('/meetups', methods=['GET'])
def getall():
    """ endpoint to fetch all meetups """

    all_meetups = MEETUPS.getall_meetups()
    if all_meetups:
        return make_response(jsonify({
            "message": "Success",
            "meetups": all_meetups
        }), 200)
    return make_response(jsonify({'message': 'Meetup not found'}), 404)

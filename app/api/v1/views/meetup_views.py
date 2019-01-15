from flask import jsonify, Blueprint, request, json, make_response
from datetime import datetime
from ..models.meetups_models import Meetup


v1_meetup_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetups = Meetup()


@v1_meetup_blueprint.route('/meetups', methods=['POST'])
def create_meetup():
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})
    """ Check for empty inputs"""
    if not all(field in data for field in ["title", "organizer", "images", "location", "happeningOn", "tags"]):
        return jsonify({"status": 400, "message": "Please fill in all the required input fields"}), 400
    """Check for data type"""

    title = data.get('title')
    createdOn = data.get('time')
    organizer = data.get('organizer')
    images = data.get("images")
    location = data.get('location')
    happeningOn = data.get('happeningOn')
    tags = data.get('tags')

    meet = jsonify(meetups.create_meetup(title, createdOn, organizer,
                                         images, location, happeningOn, tags))
    meet.status_code = 201
    return meet


@v1_meetup_blueprint.route('/meetups', methods=['GET'])
def getall():
    """ endpoint to fetch all meetups """

    data = meetups.getall_meetups()
    if data:
        return make_response(jsonify({
            "message": "Success",
            "meetups": data
        }), 200)
    return make_response(jsonify({'message': 'meetup not found'}), 404)


@v1_meetup_blueprint.route('/meetups/<int:meetup_id>', methods=['GET'])
def get_one_meetup(meetup_id):
    """querry meetups by id"""
    meetup = meetups.getone_meetup(meetup_id)
    if meetup:
        return make_response(jsonify({
            'message': 'Success',
            'meetup': meetup[0]}), 200)
    return make_response(jsonify({'message': 'meetup not found'}), 404)


@v1_meetup_blueprint.route('/meetups/<int:meetup_id>/rsvp', methods=['POST'])
def rsvp_meetup(meetup_id):
    """ endpoint for rsvp meetup """
    data = request.get_json()

    meetup = meetups.getone_meetup(meetup_id)
    if meetup:
        user_id = data.get('user_id')
        meetup_id = meetup_id
        response = data.get('response')

        res = jsonify(meetups.post_rsvp(user_id, meetup_id, response))
        res.status_code = 201
        return res
    return make_response(jsonify({'message': 'meetup not found'}), 404)

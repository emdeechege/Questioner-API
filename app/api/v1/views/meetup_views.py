from flask import jsonify, Blueprint, request, json, make_response
from ..models.meetups_models import Meetup
from datetime import datetime
from uuid import uuid4

v1_meetup_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetups = Meetup()


@v1_meetup_blueprint.route('/meetups', methods=['POST'])
def create_meetup():
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})

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
    return make_response(jsonify({
        "message": "Success",
        "meetups": data
    }), 200)


@v1_meetup_blueprint.route('/meetups/<int:meetup_id>', methods=['GET'])
def get_one_meetup(meetup_id):
    '''querry meetups by id'''
    meetup = meetups.getone_meetup(meetup_id)
    if meetup:
        return make_response(jsonify({
            'message': 'Success',
            'meetup': meetup[0]}), 200)
    return make_response(jsonify({'message': 'meetup not found'}), 404)

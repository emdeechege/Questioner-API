from flask import jsonify, Blueprint, request, json, make_response
from ..models.meetups_models import Meetup
from ..models.basemodels import login_required, admin_required

v2_meetup = Blueprint('meetup', __name__, url_prefix='/api/v2')

MEETUPS = Meetup()
# RSVP = Rsvp()


@v2_meetup.route('/meetups', methods=['POST'])
@admin_required
def create_meetup(current_user):
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
@login_required
def getall(current_user):
    """ endpoint to fetch all meetups """

    all_meetups = MEETUPS.getall_meetups()
    if all_meetups:
        return make_response(jsonify({
            "message": "Success",
            "meetups": all_meetups
        }), 200)
    return make_response(jsonify({'message': 'Meetup not found'}), 404)

@v2_meetup.route('/meetups/<int:meetup_id>', methods=['GET'])
@login_required
def get_one_meetup(current_user,meetup_id):
    """querry meetups by id"""
    meetup = MEETUPS.getone_meetup(meetup_id)
    if meetup:
        return make_response(jsonify({
            "message": "Success",
            "meetup": meetup
        })), 200
    return make_response(jsonify({'message': 'Meetup not found'}), 404)

@v2_meetup.route('/meetups/<int:meetup_id>/delete', methods=['DELETE'])
@admin_required
def delete(current_user, meetup_id):
    """deletes meetup by id"""
    one_meet = MEETUPS.getone_meetup(meetup_id)
    if one_meet:
        MEETUPS.delete_meetup(one_meet)
        return make_response(jsonify({"status": 200,\
         "Message": "Meetup {} has been deleted!"\
         .format(meetup_id)}), 200)
    return make_response(jsonify({"status": 404, 'message': 'Meetup not found'}), 404)

@v2_meetup.route('/meetups/<int:meetup_id>/rsvp', methods=['POST'])
@login_required
def rsvp_meetup(current_user, meetup_id):
    """ endpoint for rsvp meetup """
    data = request.get_json()
    if not data:
        return jsonify({"status": 400, "message": "Data set cannot be empty"}), 400

    meetup = MEETUPS.getone_meetup(meetup_id)
    if meetup:
        username = data.get('username')
        meetup_id = meetup_id
        response = data.get('response')


        rsvp = RSVP.post_rsvp(username, meetup_id, response)

        return jsonify(rsvp, {"status": 201, "message": "RSVP successful"}), 201
    return make_response(jsonify({"status": 404, 'message': 'Meetup not found'}), 404)

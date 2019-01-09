from flask import jsonify, Blueprint, request, json
from ..models.meetups_models import Meetup
from datetime import datetime
from uuid import uuid4

v1_meetup_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetup = Meetup()


@v1_meetup_blueprint.route('/meetups', methods=['POST'])
def post_meetup():
    data = request.get_json()

    meetupId = len(meetup.all_meetup_records) + 1
    createdOn = datetime.now()
    location = data["location"]
    images = data["images"]
    happeningOn = data["happeningOn"]
    tags = data["tags"]

    meetup.create_meetup(meetupId, createdOn, location, images, happeningOn, tags)
    return jsonify({
        "status": 201,
        "data": [{
            "topic": "The topic",
            "location": "The venue",
            "happeningOn": "The meetup date.",
            "tags": ["tag1", "tag2", "tag3"]
        }]
    }), 201

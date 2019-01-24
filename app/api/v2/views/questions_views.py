import json
from flask import jsonify, Blueprint, request, make_response
from ..models.questions_models import Questions
from ..models.meetups_models import Meetup
from ..models.basemodels import login_required, admin_required

v2_question = Blueprint('question', __name__, url_prefix='/api/v2')

QUESTIONS = Questions()
MEETUPS = Meetup()


@v2_question.route('/<int:meetup_id>/questions', methods=['POST'])
@login_required
def post_question(meetup_id,current_user):
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})

    if not all(field in data for field in ["title", "content"]):
        return jsonify({"status": 400, "message":\
         "Please fill in all the required input fields"}), 400

    meetup = MEETUPS.getone_meetup(meetup_id)
    if meetup:
        posted_by = current_user
        meetup_id = meetup_id
        title = data.get('title')
        content = data.get('content')

        question = QUESTIONS.post_question(
            posted_by, meetup_id, title, content)

        return jsonify(question, {
            "status": 201,
            "message": "Question added successfuly"
        }), 201
    return make_response(jsonify({'message': 'Meetup not found'}), 404)

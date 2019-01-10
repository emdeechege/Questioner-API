from flask import jsonify, Blueprint, request, json, make_response
from ..models.questions_models import Questions


v1_question_blueprint = Blueprint('questions', __name__, url_prefix='/api/v1')

questions = Questions()


@v1_question_blueprint.route('/questions', methods=['POST'])
def post_question():
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})

    postedBy = data.get('postedBy')
    meetup_id = data.get('meetup_id')
    title = data.get('title')
    content = data.get('content')
    votes = data.get('votes')

    question = jsonify(questions.post_question(postedBy, meetup_id, title, content, votes))
    question.status_code = 201

    return question

from flask import jsonify, Blueprint, request, make_response
from ..models.questions_models import Questions
from ..models.meetups_models import Meetup


v1_question_blueprint = Blueprint('questions', __name__, url_prefix='/api/v1')

QUESTIONS = Questions()
MEETUPS = Meetup()


@v1_question_blueprint.route('/questions', methods=['POST'])
def post_question():
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})

    if not all(field in data for field in ["title", "content"]):
        return jsonify({"status": 400,\
         "message": "Please fill in all the required input fields"}), 400

    posted_by = data.get('posted_by')
    meetup_id = data.get('meetup_id')
    title = data.get('title')
    content = data.get('content')

    question = QUESTIONS.post_question(
        posted_by, meetup_id, title, content)

    return question


@v1_question_blueprint.route('/questions', methods=['GET'])
def get_all_questions():
    """ endpoint to fetch all questions """

    data = QUESTIONS.getall_questions()
    return make_response(jsonify({
        "message": "Success",
        "meetups": data
    }), 200)


@v1_question_blueprint.route('/questions/<int:question_id>', methods=['GET'])
def get_one_question(question_id):
    """ check if question exists"""
    question = QUESTIONS.getone_question(question_id)
    if question:
        return make_response(jsonify({
            'message': 'Success',
            'question': question}), 200)
    return make_response(jsonify({'message': 'question not found'}), 404)


@v1_question_blueprint.route('/questions/<int:question_id>/upvote', methods=['PATCH'])
def upvotes(question_id):
    """ verifies question to be upvoted exists"""
    question = QUESTIONS.getone_question(question_id)
    if question:
        upvote = Questions().upvotes(question_id)
        return jsonify({"status": 201, "data": upvote, 'message': 'Question upvoted'})
    return make_response(jsonify({'message': 'question not found'}), 404)


@v1_question_blueprint.route('/questions/<int:question_id>/downvote', methods=['PATCH'])
def downvotes(question_id):
    """ verifies question to be downvoted exists"""
    question = QUESTIONS.getone_question(question_id)
    if question:
        downvote = Questions().downvotes(question_id)
        return jsonify({"status": 201, "data": downvote, 'message': 'Question downvoted'})
    return make_response(jsonify({'message': 'question not found'}), 404)

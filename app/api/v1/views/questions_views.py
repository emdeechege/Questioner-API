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

    question = jsonify(questions.post_question(
        postedBy, meetup_id, title, content))
    question.status_code = 201

    return question


@v1_question_blueprint.route('/questions', methods=['GET'])
def getall():
    """ endpoint to fetch all questions """

    data = questions.getall_questions()
    return make_response(jsonify({
        "message": "Success",
        "meetups": data
    }), 200)


@v1_question_blueprint.route('/questions/<int:question_id>', methods=['GET'])
def get_one_question(question_id):
    question = questions.getone_question(question_id)
    if question:
        return make_response(jsonify({
            'message': 'Success',
            'question': question[0]}), 200)
    return make_response(jsonify({'message': 'question not found'}), 404)


@v1_question_blueprint.route('/questions/<int:question_id>/upvote', methods=['PATCH'])
def upvote(question_id):
    """ endpoint for upvote question """
    one_question = questions.getone_question(question_id)
    if one_question:
        my_question = one_question[0]
        my_question["votes"] = my_question["votes"] + 1
        return make_response(jsonify({
            "status": 201,
            "data": my_question
        }), 201)


@v1_question_blueprint.route('/questions/<int:question_id>/downvote', methods=['PATCH'])
def downvote(question_id):
    """ endpoint for downvote question """
    question_id = question_id
    res = jsonify(questions.downvote_question(question_id))
    res.status_code = 201
    return res

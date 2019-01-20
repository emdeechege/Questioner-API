from flask import jsonify
from .basemodels import BaseModels, QUESTIONS_LIST, MEETUPS_LIST


class Questions(BaseModels):
    """Creates Questions model"""

    def __init__(self):
        self.db = 'questions'

    def post_question(self, posted_by, meetup_id, title, content):
        """generate new question"""
        new_question = {
            "question_id": len(QUESTIONS_LIST) + 1,
            "posted_by": posted_by,
            "meetup_id": meetup_id,
            "title": title,
            "content": content,
            "votes": 0
        }
        for record in MEETUPS_LIST:
            if record["meetup_id"] == meetup_id:
                return jsonify({"message": "Meetup does not exist"}), 404
        self.save_data(new_question)
        return jsonify(new_question, {"message": "Question added successfully"}), 201

    def getall_questions(self):
        """method to return all questions"""
        return self.check_db()

    def getone_question(self, question_id):
        """method to get one question"""
        question = self.search_db("question_id", question_id)
        return question

    def upvotes(self, question_id):
        """ search question by id and increasse vote by one"""
        qtn = self.search_db("question_id", question_id)
        if qtn['question_id'] == question_id:
            qtn['votes'] = qtn['votes'] + 1
            return qtn

    def downvotes(self, question_id):
        """ search question by id and reduce votes by one"""
        qtn = self.search_db("question_id", question_id)
        if qtn['question_id'] == question_id:
            qtn['votes'] = qtn['votes'] - 1
            return qtn

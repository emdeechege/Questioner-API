from .basemodels import BaseModels

questions = []


class Questions(BaseModels):
    """Creates Questions model"""

    def __init__(self):
        self.db = questions
        self.votes = 0


    def post_question(self, postedBy, meetup_id, title, content):
        new_question = {
            "question_id": len(questions) + 1,
            "postedBy": postedBy,
            "meetup_id": meetup_id,
            "title": title,
            "content": content,
            "votes": 0
        }

        self.db.append(new_question)
        return new_question, {"message": "Question added successfully"}

    def getall_questions(self):
        """method to return all questions"""
        return self.db

    def getone_question(self, question_id):
        """method to get one question"""
        question = self.check_item(question_id, "question_id", questions)
        return question

    def upvotes(self,question_id):
        for qtn in questions:
            if qtn['question_id'] == question_id:
                qtn['votes'] = qtn['votes'] +1
                return qtn
                
    def downvotes(self,question_id):
        for qtn in questions:
            if qtn['question_id'] == question_id:
                qtn['votes'] = qtn['votes'] -1
                return qtn

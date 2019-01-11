questions = []


class Questions:
    '''Creates Questions model'''

    def __init__(self):
        self.db = questions
        self.votes = 0

    def post_question(self, postedBy, meetup_id, title, content):
        new_question = {
            "question_id": len(questions)+1,
            "postedBy": postedBy,
            "meetup_id": meetup_id,
            "title": title,
            "content": content,
            "votes": self.votes
        }

        self.db.append(new_question)
        return new_question, {"message": "Question added successfully"}

    def getall_questions(self):
        return self.db

    def getone_question(self, question_id):
        question = [
            question for question in questions if question['question_id'] == question_id]
        return question

    def upvote_question(self, question_id):
        """ method to upvote question """

        question = [
            question for question in self.db if question['question_id'] == question_id]
        if question:
            upvote = {
                "postedBy": question[0]["postedBy"],
                "meetup_id": question[0]["meetup_id"],
                "title": question[0]["title"],
                "content": question[0]["content"],
                "votes": self.votes + 1
            }

            return upvote, {"message": "upvote successfull"}

    def downvote_question(self, question_id):
        """ method to downvote question """

        question = [
            question for question in self.db if question["question_id"] == question_id]
        if question:
            downvote = {
                "postedBy": question[0]["postedBy"],
                "meetup_id": question[0]["meetup_id"],
                "title": question[0]["title"],
                "content": question[0]["content"],
                "votes": self.votes - 1
            }

            return downvote, {"message": "downvote successfull"}

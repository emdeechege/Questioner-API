questions = []


class Questions:
    '''Creates Questions model'''

    def __init__(self):
        self.db = questions

    def post_question(self, postedBy, meetup_id, title, content, votes):
        new_question = {
            "qstn_id": len(questions)+1,
            "postedBy": postedBy,
            "meetup_id": meetup_id,
            "title": title,
            "content": content,
            "votes": votes
        }

        self.db.append(new_question)
        return new_question, {"message": "Question added successfully"}

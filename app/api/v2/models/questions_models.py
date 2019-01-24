import json
from flask import jsonify
from psycopg2.extras import RealDictCursor
from .basemodels import BaseModels


from ....connect import init_db

class Questions(BaseModels):
    """Creates Questions model"""

    def __init__(self):
        self.db = init_db()

    def post_question(self, posted_by, meetup_id, title, content):
        """generate new question"""
        new_question = {
            "posted_by": posted_by,
            "meetup_id": meetup_id,
            "title": title,
            "content": content,
            "votes": 0
        }
        cursor = self.db.cursor()
        fetch = """SELECT * FROM meetups where meetup_id = %s"""
        cursor.execute(fetch, (meetup_id, ))
        one_meetup = cursor.fetchone()
        if one_meetup:
            cursor = self.db.cursor()
            add_question = """INSERT INTO questions (meetup_id, posted_by, title, content)\
              VALUES (%(meetup_id)s, %(posted_by)s, %(title)s, %(content)s) RETURNING *"""

            cursor.execute(add_question, new_question)
            self.db.commit()
            cursor.close()
            return new_question

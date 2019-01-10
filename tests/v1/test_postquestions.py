import unittest
from app import create_app
import json


class TestQuestions(unittest.TestCase):
    '''Test Question class'''

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.question = {
            "postedBy": "user_id",
            "meetup_id": "meetup_id",
            "title": "Why now?",
            "content": "True or false",
            "votes": "votes"
        }

    def tearDown(self):
        del self.question

    def test_post_question(self):
        question = self.client.post(
            'api/v1/questions', data=json.dumps(self.question), content_type='application/json')

        self.assertEqual(question.status_code, 201)

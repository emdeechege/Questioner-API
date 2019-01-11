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
            "question_id": "question_id",
            "title": "Why now?",
            "content": "True or false",

        }
        self.upvote = {
            "postedBy": "user_id",
            "question_id": "question_id",
            "title": "Why now?",
            "content": "True or false",
            "votes": 1
        }

        self.downvote = {
            "postedBy": "user_id",
            "question_id": "question_id",
            "title": "Why now?",
            "content": "True or false",
            "votes": 1
        }

    def tearDown(self):
        del self.question

    def test_post_question(self):
        question = self.client.post(
            'api/v1/questions', data=json.dumps(self.question), content_type='application/json')

        self.assertEqual(question.status_code, 201)

    def test_all_questions_fetch(self):
        all_questions = self.client.get("api/v1/questions")

        result = json.loads(all_questions.data.decode())
        self.assertEqual(result["message"], "Success")
        self.assertEqual(all_questions.status_code, 200)

    def test_getone_question(self):
        # post one question
        question = self.client.post(
            'api/v1/questions', data=json.dumps(self.question), content_type='application/json')

        response = self.client.get("api/v1/questions/1")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "Success")
        self.assertEqual(response.status_code, 200)

    def test_get_no_question(self):
        """ tests when question id does not exist """
        response = self.client.get("api/v1/questions/6")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "question not found")
        self.assertEqual(response.status_code, 404)

    def test_upvote(self):

        upvote = self.client.patch('/api/v1/questions/1/upvote',
                                   data=json.dumps(self.upvote), content_type='application/json')

        self.assertEqual(upvote.status_code, 201)

    def test_downvote(self):
        downvote = self.client.patch('/api/v1/questions/1/downvote',
                                     data=json.dumps(self.downvote), content_type='application/json')

        self.assertEqual(downvote.status_code, 201)

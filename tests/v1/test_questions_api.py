import unittest
from app import create_app
import json


class TestQuestions(unittest.TestCase):
    """Test Question class"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.question = {
            "postedBy": 1,
            "question_id": 1,
            "title": "Why now?",
            "content": "True or false",
            "votes": 0
        }

    def tearDown(self):
        del self.question

    def test_post_question(self):
        question = self.client.post(
            'api/v1/questions', data=json.dumps(self.question), content_type='application/json')
        question_data = json.loads(question.data.decode())
        self.assertIn("Why now?", str(question_data))
        self.assertIn("Question added successfully", str(question_data))
        self.assertEqual(question.status_code, 201)


    def test_getall_questions(self):
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
        self.assertIn("Why now?", str(res))
        self.assertEqual(res["message"], "Success")
        self.assertEqual(response.status_code, 200)

    def test_get_no_question(self):
        """ tests when question id does not exist """
        response = self.client.get("api/v1/questions/6")
        res = json.loads(response.data.decode())
        self.assertIn(res["message"], "question not found")
        self.assertEqual(response.status_code, 404)

    def test_upvote_question(self):

        upvote = self.client.patch('/api/v1/questions/1/upvote',
                                   data=json.dumps(self.question), content_type='application/json')
        upvote_data = json.loads(upvote.data.decode())
        self.assertIn("upvote successfull", str(upvote_data))
        self.assertEqual(upvote.status_code, 201)

    def test_downvote_question(self):
        # post one question
        question = self.client.post(
            'api/v1/questions',  data=json.dumps(self.question), content_type='application/json')
        downvote = self.client.patch('/api/v1/questions/1/downvote',
                                     data=json.dumps(self.question), content_type='application/json')
        downvote_data = json.loads(downvote.data.decode())
        self.assertIn("downvote successfull", str(downvote_data))
        self.assertEqual(downvote.status_code, 201)

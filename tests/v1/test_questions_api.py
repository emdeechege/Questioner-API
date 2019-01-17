import unittest
import json
from app import create_app



class TestQuestions(unittest.TestCase):
    """Test Question class"""

    def setUp(self):
        self.client = create_app(config_name="testing").test_client()
        self.question = {
            "title": "Why now?",
            "content": "True or false"
        }
        self.question1 = {
            "title": "Why now?"
        }

    def tearDown(self):
        del self.question

    def test_post_question(self):
        """ tests for question creation"""
        question = self.client.post(
            'api/v1/questions', data=json.dumps(self.question), content_type='application/json')
        question_data = json.loads(question.data.decode())
        self.assertIn("Why now?", str(question_data))
        self.assertIn("Question added successfully", str(question_data))
        self.assertEqual(question.status_code, 201)

    def test_submit_empty_meetup_fields(self):
        """check for empty fields"""
        response = self.client.post(
            'api/v1/questions', data=json.dumps(self.question1), content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],
                         "Please fill in all the required input fields")
        self.assertEqual(response.status_code, 400)

    def test_getall_questions(self):
        """fetch all questions"""
        all_questions = self.client.get("api/v1/questions")

        result = json.loads(all_questions.data.decode())
        self.assertEqual(result["message"], "Success")
        self.assertEqual(all_questions.status_code, 200)

    def test_getone_question(self):
        """tests fetching one question"""
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


    def test_upvotesvotes(self):
        """upvote test"""
        question = self.client.post(
            'api/v1/questions', data=json.dumps(self.question), content_type='application/json')

        response = self.client.get("api/v1/questions/1")
        response = self.client.patch('api/v1/questions/1/upvote')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn(res["message"], "Question upvoted")

    def test_upvotesvotes_no_questions(self):
        """upvote test"""
        response = self.client.get("api/v1/questions/5")
        response = self.client.patch('api/v1/questions/5/upvote')
        res = json.loads(response.data.decode())
        self.assertIn(res["message"], "question not found")
        self.assertEqual(response.status_code, 404)


    def test_downvotes(self):
        """downvote tests"""
        question = self.client.post(
            'api/v1/questions', data=json.dumps(self.question), content_type='application/json')

        response = self.client.get("api/v1/questions/1")
        response = self.client.patch('api/v1/questions/1/downvote')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn(res["message"], "Question downvoted")

    def test_downvotesvotes_no_questions(self):
        """downvote test"""
        response = self.client.get("api/v1/questions/5")
        response = self.client.patch('api/v1/questions/5/downvote')
        res = json.loads(response.data.decode())
        self.assertIn(res["message"], "question not found")
        self.assertEqual(response.status_code, 404)

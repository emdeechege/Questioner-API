import unittest
from app import create_app
import json


class TestVoting(unittest.TestCase):
    '''Test voting class'''

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.response = {
            "postedBy": "user_id",
            "meetup_id": "meetup_id",
            "title": "Why now?",
            "content": "True or false",
            "votes": "votes"
        }

    def tearDown(self):
        del self.response

    def test_upvote(self):
        upvote = self.client.patch('/api/v1/questions/1/upvote',
                                   data=json.dumps(self.response), content_type='application/json')

        self.assertEqual(upvote.status_code, 201)

    def test_downvote(self):
        downvote = self.client.patch('/api/v1/questions/1/downvote',
                                     data=json.dumps(self.response), content_type='application/json')

        self.assertEqual(downvote.status_code, 201)

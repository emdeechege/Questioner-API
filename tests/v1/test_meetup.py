import unittest
from app import create_app
import json


class TestMeetup(unittest.TestCase):
    '''Test meetup class'''

    def setUp(self):
        '''setup method for tests'''
        self.app = create_app()
        self.client = self.app.test_client()
        self.meetup = {
            "title": "Python Hackerthon",
            "organizer": "Andela",
            "location": "Nairobi",
            "from_date": "02 01 2019 8:00am",
            "to_date":  "02 01 2019 5:00pm",
            "tags": ["python", "hackerthon"]
        }

    def tearDown(self):
        del self.meetup

    def test_api_can_create_a_meetup_record(self):
        res = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup),
                               content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("The meetup date.", str(self.meetup))
        self.assertIn("images", str(self.meetup))

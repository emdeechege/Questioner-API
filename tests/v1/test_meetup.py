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
            "images": 'me.jpg',
            "location": "Nairobi",
            "date": "02 01 2019 8:00am",
            "createdOn":  "02 01 2019 5:00pm",
            "tags": ["python", "hackerthon"]
        }

    def tearDown(self):
        del self.meetup

    def test_api_can_create_a_meetup_record(self):
        meet = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup),
                                content_type='application/json')
        self.assertEqual(meet.status_code, 201)


if __name__ == '__main__':
    unittest.main()

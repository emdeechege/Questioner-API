import unittest
from ... import create_app
import json


class TestMeetup(unittest.Testcase):
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

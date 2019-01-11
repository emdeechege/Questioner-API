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
            "happeningOn": "02 01 2019 8:00am",
            "createdOn":  "02 01 2019 5:00pm",
            "tags": ["python", "hackerthon"]
        }

        self.rsvp = {
            "user_id": "1",
            "response": "Yes"
        }

    def tearDown(self):
        del self.meetup

    def test_api_can_create_a_meetup_record(self):
        meet = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup),
                                content_type='application/json')
        self.assertEqual(meet.status_code, 201)

    def test_all_meetups_fetch(self):
        all_meetups = self.client.get("api/v1/meetups")

        result = json.loads(all_meetups.data.decode())
        self.assertEqual(result["message"], "Success")
        self.assertEqual(all_meetups.status_code, 200)

    def test_fetch_one_meetup(self):
        """ tests fetching of one meetup endpoint """
        # post a meetup
        one_meetup = self.client.post(
            "api/v1/meetups", data=json.dumps(self.meetup), content_type='application/json')
        one_meetup_data = json.loads(one_meetup.data.decode())
        self.assertIn("meetup was created successfully", str(one_meetup_data))
        self.assertEqual(one_meetup.status_code, 201)
        # feach a specific meetup
        response = self.client.get("api/v1/meetups/1")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "Success")
        self.assertEqual(response.status_code, 200)

    def test_get_no_meetup(self):
        """ tests when meetup does not exist """
        response = self.client.get("api/v1/meetups/6")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "meetup not found")
        self.assertEqual(response.status_code, 404)

    def test_rsvp_meetup(self):
        '''test for rsvp'''
        response = self.client.post("api/v1/meetups/1/rsvp",
                                    data=json.dumps(self.rsvp), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("RSVP successfull", str(res))
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()

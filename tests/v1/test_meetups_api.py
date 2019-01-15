import unittest
import json
from app import create_app



class TestMeetup(unittest.TestCase):
    """Test meetup class"""

    def setUp(self):
        """setup method for tests"""
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
        self.meetup1 ={
            "title" : "Python Hackerthon"
        }

        self.rsvp = {
            "user_id": "1",
            "response": "Yes"
        }

        self.no ={}

    def tearDown(self):
        del self.meetup

    def test_create_meetup(self):
        meet = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup),
                                content_type='application/json')
        meet_data = json.loads(meet.data.decode())
        self.assertEqual(meet.status_code, 201)
        self.assertIn("Python Hackerthon", str(meet_data))


    def test_submit_empty_meetup_fields(self):
        response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please fill in all the required input fields")
        self.assertEqual(response.status_code, 400)


    def test_getall_meetups(self):
        all_meetups = self.client.get("api/v1/meetups")

        result = json.loads(all_meetups.data.decode())
        self.assertEqual(result["message"], "Success")
        self.assertEqual(all_meetups.status_code, 200)


    def test_getone_meetup(self):
        """ tests fetching of one meetup endpoint """

        one_meetup = self.client.post(
            "api/v1/meetups", data=json.dumps(self.meetup), content_type='application/json')
        one_meetup_data = json.loads(one_meetup.data.decode())
        self.assertIn("meetup was created successfully", str(one_meetup_data))
        self.assertEqual(one_meetup.status_code, 201)

        response = self.client.get("api/v1/meetups/1")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "Success")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Python Hackerthon", str(res))

    def test_get_no_meetup(self):
        """ tests when meetup does not exist """
        response = self.client.get("api/v1/meetups/6")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "meetup not found")
        self.assertEqual(response.status_code, 404)

    def test_rsvp_meetup(self):
        """test for rsvp"""
        response = self.client.post("api/v1/meetups/1/rsvp",
                                    data=json.dumps(self.rsvp), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertIn("RSVP successfull", str(res))
        self.assertEqual(response.status_code, 201)
        self.assertIn("Yes", str(res))

    def test_rsvp_no_meetup(self):
        """test for rsvp"""
        response = self.client.post("api/v1/meetups/6/rsvp",
                                    data=json.dumps(self.rsvp), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "meetup not found")
        self.assertEqual(response.status_code, 404)



if __name__ == '__main__':
    unittest.main()

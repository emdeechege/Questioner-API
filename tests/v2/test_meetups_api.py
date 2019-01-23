import unittest
import json
from app import create_app

from app.connect import test_init_db, destroy_tests

class TestMeetup(unittest.TestCase):
    """Test meetup class"""

    def setUp(self):
        """setup method for tests"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        self.meetup = {
            "title": "Python Hackerthon",
            "organizer": "Andela",
            "images": 'me.jpg',
            "location": "Nairobi",
            "happening_on": "02 01 2019 8:00am",
            "created_on":  "02 01 2019 5:00pm",
            "tags": ["python", "hackerthon"]
        }
        self.meetup1 = {
            "title": "Python Hackerthon"
        }

        with self.app.app_context():
            self.db = test_init_db()

    def tear_down(self):
        """This function destroys objests created during the test run"""
        with self.app.app_context():
            destroy_tests()
            self.db.close()

    def test_create_meetup(self):
        """creates new meetup"""
        res = self.client.post(
            "api/v2/meetups", data=json.dumps(self.meetup), content_type='application/json')
        res_data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 201)
        self.assertIn("Python Hackerthon", str(res_data))


    def test_submit_empty_meetup_fields(self):
        """check for empty fields"""
        response = self.client.post(
            'api/v2/meetups', data=json.dumps(self.meetup1), content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],
                         "Please fill in all the required input fields")
        self.assertEqual(response.status_code, 400)

    def test_getall_meetups(self):
        """ tests fetching all meetups"""
        all_meetups = self.client.get("api/v2/meetups")

        result = json.loads(all_meetups.data.decode())
        self.assertEqual(result["message"], "Success")
        self.assertEqual(all_meetups.status_code, 200)

    def test_getone_meetup(self):
        """ tests fetching of one meetup endpoint """

        one_meetup = self.client.post(
            "api/v2/meetups", data=json.dumps(self.meetup), content_type='application/json')
        one_meetup_data = json.loads(one_meetup.data.decode())
        self.assertIn("Python Hackerthon", str(one_meetup_data))
        self.assertEqual(one_meetup.status_code, 201)

    def test_get_no_meetup(self):
        """ tests when meetup does not exist """
        response = self.client.get("api/v2/meetups/16")
        res = json.loads(response.data.decode())
        self.assertEqual(res["message"], "Meetup not found")
        self.assertEqual(response.status_code, 404)




if __name__ == '__main__':
    unittest.main()

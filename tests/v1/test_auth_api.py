import unittest
from app import create_app
import json
from app.api.v1.views import auth_views
from app.api.v1.models import auth_models


class TestUser(unittest.TestCase):
    """ Test class for user endpoints """

    def setUp(self):
        """ Defining test variables """

        self.app = create_app()
        self.client = self.app.test_client()

        self.user = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "cham@gmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "Ch@mp19?yes"
        }
        self.user4 = {
            "firstname": "Hunter",
            "lastname": "Tar",
            "othername": "Blur",
            "email": "cham@gmail.com",
            "phoneNumber": "1234756789",
            "isAdmin": "False",
            "username": "Kiboss",
            "password": "Ch@mp19?no"
        }
        self.user1 = {
            "firstname": "Angry"
        }
        self.user2 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "cham@gmail.com",
            "phoneNumber": "12345wedr",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "Ch@mp19?yes"
        }
        self.user3 = {
            "firstname": "Truthy",
            "lastname": "Stoway",
            "othername": "Birth",
            "email": "chamergmail.com",
            "phoneNumber": "1234534",
            "isAdmin": "True",
            "username": "Kijanadf",
            "password": "Ch@mp19?yes"
        }
        self.user6 = {
            "firstname": "    ",
            "lastname": "Stoway",
            "othername": "Birth",
            "email": "chamer@gmail.com",
            "phoneNumber": "1234534",
            "isAdmin": "True",
            "username": "Kijanadf",
            "password": "Ch@mp19?yes"
        }
        self.login = {
            "username": "Kijana",
            "password": "Ch@mp19?yes"
        }
        self.login1 = {
            "username": "Champ",
            "password": "Ch@mp19?yes"
        }
        self.login2 = {
            "username": "",
            "password": "Ch@mp19?yes"
        }
        self.login3 = {
            "username": "Kijana",
            "password": ""
        }
        self.login4 = {
            "username": "Kijana",
            "password": "nnmmiiijjjjuu"
        }

    def test_user_signup(self):
        """ Test signup user """

        check = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user), content_type="application/json")
        result = json.loads(check.data.decode())

        self.assertEqual(check.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertIn("Kijana", str(result))

    def test_submit_empty_signup_fields(self):
        response = self.client.post(
            '/api/v1/signup', data=json.dumps(self.user1), content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],
                         "Please fill in all the required input fields")
        self.assertEqual(response.status_code, 400)

    def test_validate_phoneNumber(self):
        response = self.client.post(
            '/api/v1/signup', data=json.dumps(self.user2), content_type="application/json")
        result = json.loads(response.data)
        self.assertTrue(result["message"],
                        "Please input valid phone number")
        self.assertTrue(response.status_code, 400)

    def test_validate_email(self):
        response = self.client.post(
            '/api/v1/signup', data=json.dumps(self.user3), content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],
                         "Invalid email")
        self.assertEqual(response.status_code, 400)

    def test_username_exists(self):
        response = self.client.post(
            '/api/v1/signup', data=json.dumps(self.user), content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],
                         "Username exists")
        self.assertEqual(response.status_code, 400)

    def test_user_login(self):
        """ Test login user """
        pass

    def test_user_exists(self):
        response1 = self.client.post(
            "/api/v1/login", data=json.dumps(self.login1), content_type="application/json")
        result1 = json.loads(response1.data.decode())

        self.assertEqual(response1.status_code, 404)
        self.assertEqual(result1["status"], 404)
        self.assertEqual(result1["message"], "User does not exist")

    def test_username_required(self):
        response2 = self.client.post(
            "/api/v1/login", data=json.dumps(self.login2), content_type="application/json")
        result2 = json.loads(response2.data.decode())

        self.assertEqual(response2.status_code, 400)
        self.assertEqual(result2["status"], 400)
        self.assertEqual(result2["message"], "Username is required")

    def test_password_required(self):

        response3 = self.client.post(
            "/api/v1/login", data=json.dumps(self.login3), content_type="application/json")
        result3 = json.loads(response3.data.decode())

        self.assertEqual(response3.status_code, 400)
        self.assertEqual(result3["status"], 400)
        self.assertEqual(result3["message"], "Password is required")

        if __name__ == "__main__":
            unittest.main()

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
            "password": "TC@ak?,T4.mm23k"
        }
        self.user1 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "cham@gmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "qwerty"
        }
        self.user2 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "chamgmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "TC@ak?,T4.mm23k"
        }
        self.user3 = {
            "firstname": "",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "chamgmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "TC@ak?,T4.mm23k"
        }
        self.user4 = {
            "firstname": "Angry",
            "lastname": "",
            "othername": "Birds",
            "email": "chamgmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "TC@ak?,T4.mm23k"
        }
        self.user5 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "TC@ak?,T4.mm23k"
        }
        self.user6 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "chamgmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": ""
        }

        self.login = {
            "username": "Kijana",
            "password": "TC@ak?,T4.mm23k"
        }
        self.login1 = {
            "username": "Kamaz",
            "password": "TC@ak?,T4.mm23k"
        }
        self.login2 = {
            "username": "",
            "password": "TC@ak?,T4.mm23k"
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

        response5 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user5), content_type="application/json")
        result5 = json.loads(response5.data.decode())

        self.assertEqual(response5.status_code, 400)
        self.assertEqual(result5["status"], 400)
        self.assertEqual(result5["message"], "Email is required")

        response6 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user6), content_type="application/json")
        result6 = json.loads(response6.data.decode())

        self.assertEqual(response6.status_code, 400)
        self.assertEqual(result6["status"], 400)
        self.assertEqual(result6["message"], "Password is required")

        return self

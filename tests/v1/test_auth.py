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
        self.user1 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "cham@gmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "labda"
        }
        self.user2 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "chamgmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "Ch@mp19?yes"
        }
        self.user3 = {
            "firstname": "",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "chamgmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "Ch@mp19?yes"
        }
        self.user4 = {
            "firstname": "Angry",
            "lastname": "",
            "othername": "Birds",
            "email": "chamgmail.com",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "Ch@mp19?yes"
        }
        self.user5 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "",
            "phoneNumber": "123456789",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "Ch@mp19?yes"
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
        self.user7 = {
            "firstname": "Angry",
            "lastname": "Stars",
            "othername": "Birds",
            "email": "chamgmail.com",
            "phoneNumber": "",
            "isAdmin": "True",
            "username": "Kijana",
            "password": "Ch@mp19?yes"
        }

        self.login = {
            "username": "Kijana",
            "password": "Ch@mp19?yes"
        }
        self.login1 = {
            "username": "Kamaz",
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

        check7 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user7), content_type="application/json")
        result7 = json.loads(check7.data.decode())

        self.assertEqual(check7.status_code, 400)
        self.assertEqual(result7["status"], 400)
        self.assertEqual(result7["message"], "Phonenumber is required")

        check1 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user1), content_type="application/json")
        result1 = json.loads(check1.data.decode())

        self.assertEqual(check1.status_code, 400)
        self.assertEqual(result1["status"], 400)
        self.assertEqual(result1["message"], "Password not valid")

        check2 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user2), content_type="application/json")
        result2 = json.loads(check2.data.decode())

        self.assertEqual(check2.status_code, 400)
        self.assertEqual(result2["status"], 400)
        self.assertEqual(result2["message"], "Invalid email")

        check3 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user3), content_type="application/json")
        result3 = json.loads(check3.data.decode())

        self.assertEqual(check3.status_code, 400)
        self.assertEqual(result3["status"], 400)
        self.assertEqual(result3["message"], "Firstname is required")

        check4 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user4), content_type="application/json")
        result4 = json.loads(check4.data.decode())

        self.assertEqual(check4.status_code, 400)
        self.assertEqual(result4["status"], 400)
        self.assertEqual(result4["message"], "Lastname is required")

        check5 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user5), content_type="application/json")
        result5 = json.loads(check5.data.decode())

        self.assertEqual(check5.status_code, 400)
        self.assertEqual(result5["status"], 400)
        self.assertEqual(result5["message"], "Email is required")

        check6 = self.client.post(
            "/api/v1/signup", data=json.dumps(self.user6), content_type="application/json")
        result6 = json.loads(check6.data.decode())

        self.assertEqual(check6.status_code, 400)
        self.assertEqual(result6["status"], 400)
        self.assertEqual(result6["message"], "Password is required")

        return self

        










        if __name__ == "__main__":
            unittest.main()

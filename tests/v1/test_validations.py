import unittest
import json
import re
from app import create_app


from app.api.v1.utils.validators import Validation


class TestValidators(unittest.TestCase):
    """ test class for validations"""

    def setUp(self):
        """ Defining test variables """

        self.client = create_app(config_name="testing").test_client()
        self.data = Validation()

    def tearDown(self):
        self.data = None

    def test_username_exists(self):
        """check if username exists"""
        username = "tom"
        users = ['tom', 'hack']
        test = self.data.username_exists(username)
        self.assertFalse(test)

    def test_email_exists(self):
        """ check if email exists"""
        email = 'tom@game.com'
        emails = ['tom@game.com', 'star@rises.net']
        test = self.data.email_exists(email)
        self.assertTrue(email in emails)

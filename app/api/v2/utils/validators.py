import re
from werkzeug.security import check_password_hash
from app.api.v1.models.auth_models import Users
from app.api.v1.models.basemodels  import BaseModels, users_list


class Validation():
    def validate_email(self, email):
        """checks the format of email is standard"""
        expects = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(expects, email)


    def validate_password(self, password):
        """check that password contains numbers, special characters and letters. Len >6"""
        expects = "r'(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[$#@]))^.{6,12}$'"
        return re.match(expects, password)

    def validate_phoneNumber(self, phoneNumber):
        """ check that phone number is digit """
        phone = "^[0-9]+$"
        return re.match(phone, phoneNumber)

    def username_exists(self, username):
        """ verifies user existence in db"""
        exists = [user for user in users_list if user['username'] == username]
        print(users_list)
        print(username)
        if exists:
            return True
        else:
            return False

    def email_exists(self, email):
        """ check if emails exist"""
        exists = [user for user in users_list if user['email'] == email]
        if exists:
            return True
        else:
            return False

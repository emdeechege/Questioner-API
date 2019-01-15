import re
from werkzeug.security import check_password_hash
from app.api.v1.models.auth_models import users


class UserValidation():
    def validate_email(self, email):
        """checks the format of email is standard"""
        exp = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(exp, email)


    def validate_password(self, password):
        """check that password contains numbers, special characters and letters. Len >6"""
        exp = "^[a-zA-Z0-9@_+-.]{6,}$"
        return re.match(exp, password)

    def username_exists(self, username):
        """ verifies user existence in db"""
        exists = [user for user in users if user['username'] == username]
        if exists:
            return True
        else:
            return False

    def same_password(self, username, password):
        """ verifies passwords match on login"""
        exists = [user for user in users if user['username'] == username]
        if exists:
            validate = check_password_hash(exists['password'], password)
            if validate:
                return True
            else:
                return False

    def email_exists(self, email):
        """ check if emails exist"""
        exists = [user for user in users if user['email'] == email]
        if exists:
            return True
        else:
            return False

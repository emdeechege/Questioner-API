import re
from werkzeug.security import check_password_hash
from app.api.v1.models.auth_models import users


class UserValidation():
    def validate_email(self, email):
        exp = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(exp, email)


    def validate_password(self, password):
        exp = "^[a-zA-Z0-9@_+-.]{3,}$"
        return re.match(exp, password)

    def username_exists(self, username):
        exists = [user for user in users if user['username'] == username]
        if exists:
            return True
        else:
            return False

    def same_password(self, username, password):
        exists = [user for user in users if user['username'] == username]
        if exists:
            validate = check_password_hash(exists['password'], password)
            if validate:
                return True
            else:
                return False

    def email_exists(self, email):
        exists = [user for user in users if user['email'] == email]
        if exists:
            return True
        else:
            return False

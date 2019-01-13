import jwt
import os
from datetime import datetime, timedelta
from instance.config import Config

users = []
SECRET_KEY = Config.SECRET_KEY
token = {}


class Users():
    """ A class that maps user data """

    def __init__(self):
        self.db = users

    def generate_auth_token(self, username):
        """ Generate auth token """
        try:
            payload = {'exp': datetime.utcnow() + timedelta(days=0, seconds=120),
                       'iat': datetime.utcnow(), 'sub': username}
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        except Exception as e:
            return e

    def verify_auth_token(self, auth_token):
        """Verify auth token """
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token exppired, login again'
        except jwt.InvalidTokenError:
            return 'Invalid token, login'

    def signup(self, firstname, lastname, othername, email, phoneNumber, username, isAdmin, password):
        registered = datetime.now()
        new_user = {
            "user_id": len(users) + 1,
            "firstname": firstname,
            "lastname": lastname,
            "othername": othername,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "registered": registered,
            "isAdmin": isAdmin,
            "password": password
        }

        self.db.append(new_user)
        return new_user, {"message": "User was created successfully"}

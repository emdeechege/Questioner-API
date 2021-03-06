from flask import jsonify
import jwt
from datetime import datetime, timedelta
from instance.config import Config
from .basemodels import BaseModels, USERS_LIST


SECRET_KEY = Config.SECRET_KEY



class Users(BaseModels):
    """ A class that maps user data """
    def __init__(self):
        self.db = 'user'

    def generate_auth_token(self, username):
        """ Generate auth token """
        try:
            payload = {'exp': datetime.utcnow() + timedelta(days=0, seconds=180),
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
            return 'Token expired, login again'
        except jwt.InvalidTokenError:
            return 'Invalid token, login'

    def signup(self, firstname, lastname, othername, email, phone_number,\
     username, is_admin, password):
        """collects and creates signup details"""
        registered = datetime.now()
        user = {
            "user_id": len(USERS_LIST) + 1,
            "firstname": firstname,
            "lastname": lastname,
            "othername": othername,
            "email": email,
            "phone_number": phone_number,
            "username": username,
            "registered": registered,
            "is_admin": is_admin,
            "password": password
        }

        self.save_data(user)
        return user, {"message": "User was created successfully"}

    def login(self, username, password):
        """logs in a user"""
        data = self.search_db("username", username)
        if data:
            if data["password"] == password:
                return jsonify({"message": "successfully signed-in as {}".format(username)}), 200
            return jsonify({"message": "invalid username or password"}), 403
        return jsonify({"message": "user {} was not found".format(username)}), 404

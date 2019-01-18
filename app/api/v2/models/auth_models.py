from datetime import datetime, timedelta
import jwt

from instance.config import Config
from .basemodels import BaseModels
from ....connect import init_db


SECRET_KEY = Config.SECRET_KEY
token = {}


class Users(BaseModels):
    """ A class that maps user data """
    def __init__(self):
         """initialize the user model"""
         self.db = init_db()


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

    def signup(self, firstname=None, lastname=None, othername=None, email=None, phoneNumber=None, username=None, isAdmin=False, password=None):
        """collects and creates signup details"""
        registered = datetime.now()
        user = {
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

        cursor = self.db .cursor()
        query = """INSERT INTO users (firstname, lastname, othername, email, phoneNumber, username, isAdmin, password) \
        VALUES (%(firstname)s, %(lastname)s, %(othername)s, %(email)s, %(phoneNumber)s, %(username)s, \
        %(isAdmin)s, %(password)s) RETURNING user_id"""
        cursor.execute(query, user)
        user_id = cursor.fetchone()[0]
        self.db .commit()
        cursor.close()
        return int(user_id)

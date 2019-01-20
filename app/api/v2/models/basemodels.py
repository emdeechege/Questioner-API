import jwt
from datetime import datetime, timedelta
from flask import jsonify, make_response
from instance.config import Config


from app.connect import init_db

SECRET_KEY = Config.SECRET_KEY
token = {}

class BaseModels(object):
    """ contains methods common to other models """
    def __init__(self):
        """initialize the database"""
        self.db = init_db()

    def update_item(self, table, field, data, item_field, item_id):
        """update the field of an item given the item_id"""

        dbconn = self.db
        curr = dbconn.cursor()
        updated = curr.execute("UPDATE {} SET {}='{}' \
                     WHERE {} = {} ;".format(table, field, data, item_field, item_id))
        dbconn.commit()
        if updated:
            return True


    def check_exists(self, username):
        """Check if the records exist"""
        curr = self.db.cursor()
        query = "SELECT username FROM users WHERE username = '%s'" % (username)
        curr.execute(query)
        return curr.fetchone() is not None

    @staticmethod
    def generate_auth_token(self, username):
        """ Generate auth token """
        try:
            payload = {'exp': datetime.utcnow() + timedelta(days=0, seconds=180),
                       'iat': datetime.utcnow(), 'sub': username}
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        except Exception as e:
            return e

    @staticmethod
    def verify_auth_token(self, auth_token):
        """Verify auth token """
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token expired, login again'
        except jwt.InvalidTokenError:
            return 'Invalid token, login'

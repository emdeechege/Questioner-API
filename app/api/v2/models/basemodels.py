import jwt
from functools import wraps
from datetime import datetime, timedelta
from flask import jsonify, make_response, request
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


    @staticmethod
    def generate_auth_token(username):
        """ Generate auth token """
        try:
            payload = {'exp': datetime.utcnow() + timedelta(days=1, seconds=180),
                       'iat': datetime.utcnow(), 'sub': username}
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        except Exception as e:
            return e

def login_required(f):
    """ User authentication function """
    @wraps(f)
    def authenticate(*args, **kwargs):
        """ decorator for login authentication """
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            try:
                payload = jwt.decode(
                    token, SECRET_KEY,algorithm='HS256')
            except jwt.ExpiredSignatureError:
                return jsonify({
                    'status': 401,
                    'error': 'Your session has expired. Please login again'
                }), 401
        user = payload['sub']

        if user:
            return f(*args,**kwargs)
        return jsonify({
            "status": 404,
            "error": "User not found"
        }), 404

    return authenticate

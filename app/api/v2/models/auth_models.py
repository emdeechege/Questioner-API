from datetime import datetime, timedelta
from flask import jsonify


from app.connect import QuestionerDB
from .basemodels import BaseModels
# from ....connect import init_db

class Users(BaseModels):
    """ A class that maps user data """

    def __init__(self):
        """initialize the user model"""
        self.db = QuestionerDB

    def signup(self, firstname=None, lastname=None, othername=None, email=None,
               phone_number=None, username=None, is_admin=False, password=None):
        """collects and creates signup details"""
        registered = datetime.now()
        user = {
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
        cursor = self.db.conn.cursor()
        query = """INSERT INTO users (firstname, lastname,\
         othername, email, phone_number, username, is_admin, password) \
        VALUES (%(firstname)s, %(lastname)s, %(othername)s, %(email)s, %(phone_number)s, %(username)s, \
        %(is_admin)s, %(password)s)"""
        cursor.execute(query,user)
        self.db.conn.commit()
        cursor.close()
        return user

from datetime import datetime, timedelta
from flask import jsonify



from .basemodels import BaseModels
from ....connect import init_db

class Users(BaseModels):
    """ A class that maps user data """

    def __init__(self):
        """initialize the user model"""
        self.db = init_db()

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

        cursor = self.db .cursor()
        query = """INSERT INTO users (firstname, lastname,\
         othername, email, phone_number, username, is_admin, password) \
        VALUES (%(firstname)s, %(lastname)s, %(othername)s, %(email)s, %(phone_number)s, %(username)s, \
        %(is_admin)s, %(password)s) RETURNING username"""

        cursor.execute(query, user)
        username = cursor.fetchone()[0]
        self.db .commit()
        cursor.close()
        return username

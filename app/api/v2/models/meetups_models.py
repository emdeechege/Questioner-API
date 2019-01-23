from flask import jsonify
from datetime import datetime
from psycopg2.extras import RealDictCursor
from .basemodels import BaseModels


from ....connect import init_db

class Meetup(BaseModels):
    """ Creates the meetup record model """

    def __init__(self):
        self.db = init_db()

    def create_meetup(self, title=None, organizer=None, images=None,\
     location=None, happening_on=None, tags=None):
        """ method to add meetup """
        new_meetup = {
            "title": title,
            "organizer": organizer,
            "images": images,
            "created_on": datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            "location": location,
            "happening_on": happening_on,
            "tags": tags
        }

        cursor = self.db.cursor()
        add_meetup = """INSERT INTO meetups (title, organizer,\
         images, location, happening_on, tags)\
          VALUES (%(title)s, %(organizer)s, %(images)s, %(location)s, \
          %(happening_on)s, %(tags)s) RETURNING *"""

        cursor.execute(add_meetup, new_meetup)
        self.db.commit()
        cursor.close()
        return new_meetup

    def getall_meetups(self):
        ''' method to fetch all the posted meetups '''
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        fetch = "SELECT * FROM meetups"
        cursor.execute(fetch)
        meetups = cursor.fetchall()
        cursor.close()
        return meetups

    def getone_meetup(self, meetup_id):
        ''' method to get specific meetup based on its id '''
        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        fetch = """SELECT * FROM meetups where meetup_id = %s"""
        cursor.execute(fetch, (meetup_id, ))
        one_meetup = cursor.fetchone()
        return one_meetup

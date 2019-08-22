from datetime import datetime
from psycopg2.extras import RealDictCursor
from .basemodels import BaseModels

from app.connect import QuestionerDB
# from ....connect import init_db


class Meetup(BaseModels):
    """ Creates the meetup record model """

    def __init__(self):
        self.db = QuestionerDB

    def create_meetup(self, title, organizer, images,
                      location, happening_on, tags):
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

        cursor = self.db.conn.cursor()
        add_meetup = """INSERT INTO meetups (title, organizer,\
         images, location, happening_on, tags)\
          VALUES (%(title)s, %(organizer)s, %(images)s, %(location)s, \
          %(happening_on)s, %(tags)s) RETURNING *"""

        cursor.execute(add_meetup, new_meetup)
        self.db.conn.commit()
        cursor.close()
        return new_meetup

    def getall_meetups(self):
        ''' method to fetch all the posted meetups '''
        cursor = self.db.conn.cursor(cursor_factory=RealDictCursor)
        fetch = "SELECT * FROM meetups"
        cursor.execute(fetch)
        meetups = cursor.fetchall()
        cursor.close()
        return meetups

    def getone_meetup(self, meetup_id):
        ''' method to get specific meetup based on its id '''
        cursor = self.db.conn.cursor(cursor_factory=RealDictCursor)
        fetch = """SELECT * FROM meetups where meetup_id = %s"""
        cursor.execute(fetch, (meetup_id, ))
        one_meetup = cursor.fetchone()
        cursor.close()
        return one_meetup

    def delete_meetup(self, meetup_id):
        """This methods deletes a meetup from the db based on the its meetup_id number."""
        cursor = self.db.conn.cursor()
        delete = """DELETE FROM meetups WHERE meetup_id = %s"""
        cursor.execute(delete, (meetup_id, ))
        self.db.conn.commit()
        cursor.close()
        return {"status": 200, "Message": "Meetup deleted"}


class Rsvp(BaseModels):
    """ Creates the RSVP record model """

    def __init__(self):
        self.db = QuestionerDB

    def post_rsvp(self, username, meetup_id, response):
        """ method for rsvp meetup """
        new_rsvp = {
            "meetup_id": meetup_id,
            "username": username,
            "response": response
        }
        cursor = self.db.cursor()
        fetch = """SELECT * FROM meetups where meetup_id = %s"""
        cursor.execute(fetch, (meetup_id, ))
        one_meetup = cursor.fetchone()
        if one_meetup:

            sql = """INSERT INTO rsvp (meetup_id, username, response)
                 VALUES(%(meetup_id)s, %(username)s, %(response)s) RETURNING rsvp_id"""
            cursor.execute(sql, new_rsvp)
            self.db.conn.commit()
            cursor.close()
            return new_rsvp

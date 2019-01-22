from flask import jsonify
from datetime import datetime
from .basemodels import BaseModels

from ....connect import init_db

class Meetup(BaseModels):
    """ Creates the meetup record model """

    def __init__(self):
        self.db = init_db()

    def create_meetup(self, title, organizer, images, location, happening_on, tags):
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
          VALUES (%(title)s, %(organizer)s, %(location)s, \
          %(happening_onl)s, %(tag)s) RETURNING meetup_id"""

        cursor.execute(add_meetup, new_meetup)
        meetup_id = cursor.fetchone()[0]
        self.db.commit()
        cursor.close()
        return int(meetup_id)

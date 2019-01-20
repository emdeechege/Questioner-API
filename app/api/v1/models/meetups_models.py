from flask import jsonify
from datetime import datetime
from .basemodels import BaseModels, MEETUPS_LIST, RSVP_LIST


class Meetup(BaseModels):
    """ Creates the meetup record model """

    def __init__(self):
        self.db = 'meetups'

    def create_meetup(self, title, organizer, images, location, happening_on, tags):
        """ method to add meetup """
        new_meetup = {
            "meetup_id": len(MEETUPS_LIST) + 1,
            "title": title,
            "organizer": organizer,
            "images": images,
            "created_on": datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            "location": location,
            "happening_on": happening_on,
            "tags": tags
        }

        self.save_data(new_meetup)
        return new_meetup, {"message": "Meetup added successfully"}

    def getall_meetups(self):
        """method to get all meetups"""
        return self.check_db()

    def getone_meetup(self, meetup_id):
        """method to fetch one meetup"""
        meetup = self.search_db("meetup_id", meetup_id)
        return meetup


class Rsvp(BaseModels):
    """ Creates the RSVP record model """
    def __init__(self):
        self.db = 'rsvp'

    def post_rsvp(self, user_id, meetup_id, response):
        """ method for rsvp meetup """
        new_rsvp = {
            "rsvp_id": len(RSVP_LIST) + 1,
            "user_id": user_id,
            "meetup_id": meetup_id,
            "response": response
        }
        data = self.search_meetup("meetup_id", meetup_id)
        if data:
            self.save_data(new_rsvp)
            return jsonify(new_rsvp, {"message": "RSVP successful"}), 201
        else:
            return jsonify({"message": "Meetup not found"}), 404

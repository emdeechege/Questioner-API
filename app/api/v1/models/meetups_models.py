from flask import jsonify
from datetime import datetime
from .basemodels import BaseModels, meetups_list, rsvp_list


class Meetup(BaseModels):
    """ Creates the meetup record model """

    def __init__(self):
        self.db = 'meetups'
        self.now = datetime.now().strftime("%H:%M%P %A %d %B %Y"),

    def create_meetup(self, title, createdOn, organizer, images, location, happeningOn, tags):
        """ method to add meetup """
        new = {
            "meetup_id": len(meetups_list) + 1,
            "title": title,
            "organizer": organizer,
            "images": images,
            "createdOn": self.now,
            "location": location,
            "happeningOn": happeningOn,
            "tags": tags
        }

        self.save_data(new)
        return new, {"message": "Meetup added successfully"}

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
        new = {
            "rsvp_id": len(rsvp_list) + 1,
            "user_id": user_id,
            "meetup_id": meetup_id,
            "response": response
        }

        data = self.search_db("meetup_id", meetup_id)
        if data:
            self.save_data(new)
            return jsonify(new, {"message": "RSVP successful"}), 201
        else:
            return jsonify({"message": "Meetup not found"}), 404

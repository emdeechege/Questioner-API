from datetime import datetime
from .basemodels import BaseModels

meetups = []
rsvp = []


class Meetup(BaseModels):
    """ Creates the meetup record model """

    def __init__(self):
        self.db = meetups
        self.rsvp = rsvp
        self.now = datetime.now().strftime("%H:%M%P %A %d %B %Y"),

    def create_meetup(self, title, createdOn, organizer, images, location, happeningOn, tags):
        """ method to add meetup """
        new_meetup = {
            "meetup_id": len(meetups) + 1,
            "title": title,
            "organizer": organizer,
            "images": images,
            "createdOn": self.now,
            "location": location,
            "happeningOn": happeningOn,
            "tags": tags
        }

        self.db.append(new_meetup)
        return new_meetup, {"message": "meetup was created successfully"}

    def getall_meetups(self):
        """method to get all meetups"""
        return self.db

    def getone_meetup(self, meetup_id):
        meetup = self.check_item(meetup_id, "meetup_id", meetups)
        return meetup

    def post_rsvp(self, user_id, meetup_id, response):
        """ method for rsvp meetup """
        rsvp = {
            "rsvp_id": len(self.rsvp) + 1,
            "user_id": user_id,
            "meetup_id": meetup_id,
            "response": response
        }

        self.rsvp.append(rsvp)
        return rsvp, {"message": "RSVP successfull"}

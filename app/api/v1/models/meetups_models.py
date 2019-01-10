from datetime import datetime

meetups = []


class Meetup:
    """ Creates the meetup record model """

    def __init__(self):
        self.db = meetups
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
        return self.db

    def getone_meetup(self, meetupId):
        meetup = [meetup for meetup in meetups if meetup["meetup_id"] == meetupId]
        return meetup

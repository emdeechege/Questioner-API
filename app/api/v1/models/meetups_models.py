from datetime import datetime

meetups = []


class Meetup:
    """ Creates the meetup record model """

    def __init__(self):
        self.db = meetups
        self.id = len(meetups) + 1
        self.now = datetime.now().strftime("%H:%M%P %A %d %B %Y"),

    def create_meetup(self, title, createdOn, organizer, images, location, happeningOn, tags):
        """ method to add meetup """
        new_meetup = {
            "meetup_id": self.id,
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

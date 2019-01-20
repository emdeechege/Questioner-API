"""all storage and common methods stored here"""
USERS_LIST = []
QUESTIONS_LIST = []
MEETUPS_LIST = []
RSVP_LIST = []


class BaseModels(object):
    """ contains methods common to other models """

    def __init__(self, db):
        self.db = db

    def check_db(self):
        """matches db in other models"""
        if self.db == 'user':
            db = USERS_LIST
            return db
        elif self.db == 'questions':
            db = QUESTIONS_LIST
            return db
        elif self.db == 'meetups':
            db = MEETUPS_LIST
            return db

        elif self.db == 'rsvp':
            db = RSVP_LIST
            return db

    def search_db(self, key, item):
        """checks for specified items in db"""
        db = self.check_db()
        data = [record for record in db if record[key] == item]
        if data:
            return data[0]
        else:
            return False

    def check_item(self, item, key, db):
        """checks for data in dictionaries"""
        data = [record for record in db if record[key] == item]
        return data

    def save_data(self, new):
        """ method appends data to relevant lists"""
        db = self.check_db()
        db.append(new)

        return db

    @classmethod
    def questions_meetups(cls):
        """append questions to meetups"""
        for meetup in MEETUPS_LIST:
            for question in QUESTIONS_LIST:
                if meetup["meetup_id"] == question["meetup"]:
                    meetups = MEETUPS_LIST.append(question)
                    return meetups

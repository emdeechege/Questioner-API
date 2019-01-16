users_list = []
questions_list = []
meetups_list = []
rsvp_list = []


class BaseModels(object):
    """ contains methods common to other models """

    def __init__(self, db):
        self.db = db

    def check_db(self):
        if self.db == 'user':
            db = users_list
            return db
        elif self.db == 'questions':
            db = questions_list
            return db
        elif self.db == 'meetups':
            db = meetups_list
            return db

        elif self.db == 'rsvp':
            db = rsvp_list
            return db

    def search_db(self, key, item):
        db = self.check_db()
        data = [record for record in db if record[key] == item]
        if data:
            return data[0]
        else:
            return False

    def search_meetup(self, key, item):
        data = [record for record in meetups_list if record[key] == item]
        if data:
            return data[0]
        else:
            return False

    def search_username(self, key, item):
        data = [record for record in users_list if record[key] == item]
        if data:
            return data[0]
        else:
            return False

    def check_item(self, item, key, db):
        """checks for data in dictionaries"""
        data = [record for record in db if record[key] == item]
        return data

    def save_data(self, new):
        db = self.check_db()
        db.append(new)

        return db

    @classmethod
    def questions_meetups(cls):
        for meetup in meetups_list:
            for question in questions_list:
                if meetup["meetup_id"] == question["meetup"]:
                    meetups = meetups_list.append(question)
                    return meetups

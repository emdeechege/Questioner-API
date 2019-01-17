from flask import jsonify, make_response

from app.connect import init_db


class BaseModels(object):
    """ contains methods common to other models """
    def __init__(self):
        """initialize the database"""
        self.db = init_db()

    def update_item(self, table, field, data, item_field, item_id):
        """update the field of an item given the item_id"""

        dbconn = self.db
        curr = dbconn.cursor()
        updated = curr.execute("UPDATE {} SET {}='{}' \
                     WHERE {} = {} ;".format(table, field, data, item_field, item_id))
        dbconn.commit()
        if updated:
            return True


    def check_exists(self, table, field, data):
        """Check if the records exist"""
        curr = self.db.cursor()
        query = "SELECT * FROM {} WHERE {}={};".format(table, field, data)
        curr.execute(query)
        data = curr.fetchone()
        if data:
            return True
        else:
            return False

class BaseModels(object):
    """ contains methods common to other models """

    def check_item(self, item, key, db):
        """checks for data in dictionaries"""
        data = [record for record in db if record[key] == item]
        return data

    def payload(self, items, keys):
        items = items.keys()
        if len(items) == len(keys):
            for item in items:
                if item not in keys:
                    return False
            return True
        else:
            return False

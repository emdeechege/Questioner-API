import re


class Validation():
    """contains validation criteria for authorization"""
    def validate_email(self, email):
        """checks the format of email is standard"""
        expects = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(expects, email)


    def validate_password(self, password):
        """check that password contains numbers, special characters and letters. Len >6"""
        expects = "r'(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[$#@]))^.{6,12}$'"
        return re.match(expects, password)

    def validate_phone_number(self, phone_number):
        """ check that phone number is digit """
        phone = "^[0-9]+$"
        return re.match(phone, phone_number)

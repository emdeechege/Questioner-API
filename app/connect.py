import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app
from app import schema
from werkzeug.security import generate_password_hash, check_password_hash


class QuestionerDB():
    """Class with database connection"""

    @classmethod
    def init_db(cls, url):
        """ setup database connection"""

        cls.conn = psycopg2.connect(url)
        cls.curr = cls.conn.cursor()

    @classmethod
    def create_tables(cls):
        queries = schema.tables()

        for query in queries:
            cls.curr.execute(query)
        cls.conn.commit()
        QuestionerDB.admin()

    @classmethod
    def admin(cls):
        username = "Admin"
        is_admin = True
        password = "Champ@123#"
        hashed = generate_password_hash(
            password, method='pbkdf2:sha256', salt_length=8)
        query = """SELECT * FROM users WHERE username = '{}'""".format(
            username)
        cls.curr.execute(query)
        admin = cls.curr.fetchone()
        if not admin:

            admin = """INSERT INTO users (firstname,lastname,phone_number,username,email,password,is_admin) \
                      VALUES ('Emdee', 'Chege', '0725222520', 'Admin', 'staremdee@gmail.com', '{}', True )
                """.format(hashed)
            cls.curr.execute(admin)
            cls.conn.commit()

    @classmethod
    def drop_tables(cls):
        """Method to delete tables"""
        query = """DROP TABLE IF EXISTS users, meetups, questions, rsvp,\
        comments CASCADE;"""
        cls.curr.execute(query)
        cls.conn.commit()
        cls.conn.close()

    @classmethod
    def save_data(cls, query):
        """Save data into tables"""
        cls.curr.execute(query)
        cls.conn.commit()
        data = cls.curr.fetchone()[0]
        return data

    @classmethod
    def fetch_one(cls, query):
        """Method to fetch specific item"""
        cls.curr.execute(query)
        return cls.curr.fetchone()

    @classmethod
    def fetch_all(cls, query):
        """Method to fetch all items"""
        cls.curr.execute(query)
        return cls.curr.fetchall()

    @classmethod
    def remove_one(cls, query):
        """Method to delete record"""
        cls.curr.execute(query)
        cls.conn.commit()

# def test_init_db():
#     """set up db testing environment"""
#
#     conn = psycopg2.connect(os.getenv("DATABASE_TEST_URL"))
#     curr = conn.cursor()
#     queries = schema.tables()
#
#     for query in queries:
#         curr.execute(query)
#     conn.commit()
#     return conn


# def destroy():
#     """Drops tables on request"""
#
#     conn = psycopg2.connect(os.getenv("DATABASE_URL"))
#     curr = conn.cursor()
#     users = "DROP TABLE IF EXISTS users CASCADE"
#     meetups = "DROP TABLE IF EXISTS meetups CASCADE"
#     questions = "DROP TABLE IF EXISTS questions CASCADE"
#     rsvp = "DROP TABLE IF EXISTS rsvp CASCADE"
#     comments = "DROP TABLE IF EXISTS comments CASCADE"
#     queries = [users, meetups, questions, rsvp, comments]
#     try:
#         for query in queries:
#             curr.execute(query)
#         conn.commit()
#         conn.close()
#     except:
#         return "Tables not dropped"
#
#
# def destroy_tests():
#     """tear down for db after tests"""
#
#     conn = psycopg2.connect(os.getenv("DATABASE_TEST_URL"))
#     curr = conn.cursor()
#     users = "DROP TABLE IF EXISTS users CASCADE"
#     meetups = "DROP TABLE IF EXISTS meetups CASCADE"
#     questions = "DROP TABLE IF EXISTS questions CASCADE"
#     rsvp = "DROP TABLE IF EXISTS rsvp CASCADE"
#     comments = "DROP TABLE IF EXISTS comments CASCADE"
#     queries = [users, meetups, questions, rsvp, comments]
#     try:
#         for query in queries:
#             curr.execute(query)
#         conn.commit()
#         conn.close()
#     except:
#         return "Tables not dropped"

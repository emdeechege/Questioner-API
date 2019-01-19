import os
import psycopg2

from app import schema
from instance.config import Config



def init_db():
    """ setup database connection"""

    conn = psycopg2.connect("dbname=questioner user=emdee password=arif@123")
    curr = conn.cursor()
    queries = schema.tables()

    for query in queries:
        curr.execute(query)
    conn.commit()
    return conn

def connect():
    conn = psycopg2.connect("dbname=questioner user=emdee password=arif@123")
    return conn

def test_init_db():
    """set up db testing environment"""

    conn = psycopg2.connect("dbname=questioner_test user=emdee password=arif@123")
    curr = conn.cursor()
    queries = schema.tables()

    for query in queries:
        curr.execute(query)
    conn.commit()
    return conn

def destroy():
    """Drops tables on request"""

    conn = psycopg2.connect("dbname=questioner user=emdee password=arif@123")
    curr = conn.cursor()
    users = "DROP TABLE IF EXISTS users CASCADE"
    meetups = "DROP TABLE IF EXISTS meetups CASCADE"
    questions = "DROP TABLE IF EXISTS questions CASCADE"
    rsvp = "DROP TABLE IF EXISTS rsvp CASCADE"
    comments = "DROP TABLE IF EXISTS comments CASCADE"
    queries = [users, meetups, questions, rsvp, comments]
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
    except:
        return "Tables not dropped"


def destroy_tests():
    """tear down for db after tests"""

    conn = psycopg2.connect("dbname=questioner_test user=emdee password=arif@123")
    curr = conn.cursor()
    users = "DROP TABLE IF EXISTS users CASCADE"
    meetups = "DROP TABLE IF EXISTS meetups CASCADE"
    questions = "DROP TABLE IF EXISTS questions CASCADE"
    rsvp = "DROP TABLE IF EXISTS rsvp CASCADE"
    comments = "DROP TABLE IF EXISTS comments CASCADE"
    queries = [users, meetups, questions, rsvp, comments]
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
    except:
        return "Tables not dropped"

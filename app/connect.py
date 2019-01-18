import os
import psycopg2

from app import schema
from instance.config import Config



def init_db():
    """ setup database connection"""

    conn = psycopg2.connect("dbname=questioner user=emdee password=arif@123")
    conn.commit()
    return conn

def connect():
    conn = psycopg2.connect("dbname=questioner user=emdee password=arif@123")
    return conn

def test_init_db():
    """set up db testing environment"""

    conn = psycopg2.connect("dbname=questioner_test user=emdee password=arif@123")
    destroy()
    conn.commit()
    return conn

def create_tables(conn):
    curr = conn.cursor()
    queries = schema.tables()

    for query in queries:
        curr.execute(query)
    conn.commit()

def destroy():
    """tear down for db during after tests"""

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

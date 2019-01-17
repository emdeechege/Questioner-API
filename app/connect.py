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
    queries = tables()

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

""" holds database information in tabular format"""
def tables():
    """ defines database table structures"""

    users = """CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY NOT NULL,
        firstname character varying(50) NOT NULL,
        lastname  character varying(50) NOT NULL,
        othername character varying(50) NOT NULL,
        email  character varying(50) UNIQUE,
        phoneNumber numeric NOT NULL,
        username character varying(50) NOT NULL,
        password character varying(50) NOT NULL,
        isAdmin BOOLEAN NOT NULL DEFAULT FALSE,
        registered timestamp default current_timestamp
    );"""

    meetups = """CREATE TABLE IF NOT EXISTS meetups(
        id serial PRIMARY KEY NOT NULL,
        happenningOn date NOT NULL,
        location character varying(50) NULL,
        images text NULL,
        topic character varying(200) NOT NULL,
        tags text NULL,
        createdOn timestamp default current_timestamp
    );"""


    questions = """CREATE TABLE IF NOT EXISTS questions(
        id serial PRIMARY KEY NOT NULL,
        meetup_id numeric NOT NULL,
        user_id numeric NOT NULL,
        postedBy numeric NOT NULL,
        title character varying(200) NOT NULL,
        body text NOT NULL,
        votes integer DEFAULT 0,
        createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""

    rsvps = """CREATE TABLE IF NOT EXISTS rsvps(
        id serial PRIMARY KEY NOT NULL,
        meetup_id numeric NOT NULL,
        user_id numeric NOT NULL,
        response character varying(30) NOT NULL
    );"""

    queries = [users, meetups, questions, rsvps]

    return queries

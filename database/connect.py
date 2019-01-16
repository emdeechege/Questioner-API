import psycopg2
import os
from flask import current_app
from database import migrations

def db_init():
    """ setup database connection"""
    url = current_app.config['DATABASE_URL']
    conn = psycopg2.connect(url)
    conn.commit()
    return conn

def connect(url):
    conn = psycopg2.connect(url)
    return conn

def test_db_init():
    """set up db testing environment"""
    test_url = os.getenv('DATABASE_TEST_URL')
    conn = psycopg2.connect(test_url)
    destroy()
    conn.commit()
    return conn

def create_tables(conn):
    curr = conn.cursor()
    tables = migrations.tables()

    for query in tables:
        curr.execute(query)
    conn.commit()

def destroy():
    """tear down for db during after tests"""
    test_url = current_app.config['DATABASE_TEST_URL']
    conn = connect(test_url)
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

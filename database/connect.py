import psycopg2
from flask import current_app


def connect(url):
    """connects to Postgres server"""

    url = current_app.config.get('  DATABASE_URL')
    try:
        conn = psycopg2.connect(url)
        return conn
    except psycopg2.DatabaseError as e:
        return {"message": '{}.format(e)'}

def db_init():
    """ setup database connection"""
    url = current_app.config['DATABASE_URL']
    conn = connect(url)
    return conn

def test_db_init():
    """set up db testing environment"""
    url = current_app.config['DATABASE_URL']
    conn = connect(url)
    create_tables(conn)

def create_tables(conn):
    curr = conn.cursor()
    tables = migrations.tables()

    for query in tables:
        curr.execute(query)
    conn.commit()

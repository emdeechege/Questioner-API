""" holds database information in tabular format"""

def tables():
    """ defines database table structures"""

    users = """CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        firstname character varying(50) NOT NULL,
        lastname  character varying(50) NOT NULL,
        othername character varying(50) NOT NULL,
        email  character varying(70) UNIQUE,
        phone_number numeric NOT NULL,
        username character varying(50) NOT NULL,
        password character varying(1000) NOT NULL,
        is_admin BOOLEAN NOT NULL DEFAULT FALSE,
        registered timestamp default current_timestamp
    );"""

    meetups = """CREATE TABLE IF NOT EXISTS meetups(
        meetup_id serial PRIMARY KEY NOT NULL,
        happenning_on date NOT NULL,
        location character varying(50) NULL,
        images text NULL,
        topic character varying(200) NOT NULL,
        tags text NULL,
        created_on timestamp default current_timestamp
    );"""


    questions = """CREATE TABLE IF NOT EXISTS questions(
        question_id serial PRIMARY KEY NOT NULL,
        meetup_id numeric NOT NULL,
        user_id numeric NOT NULL,
        posted_by numeric NOT NULL,
        title character varying(200) NOT NULL,
        body text NOT NULL,
        votes integer DEFAULT 0,
        createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""

    rsvp = """CREATE TABLE IF NOT EXISTS rsvp(
        id serial PRIMARY KEY NOT NULL,
        meetup_id numeric NOT NULL,
        user_id numeric NOT NULL,
        response character varying(30) NOT NULL
    );"""

    queries = [users, meetups, questions, rsvp]

    return queries

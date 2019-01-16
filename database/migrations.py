""" holds database information in tabular format"""
def tables():
    """ defines database table structures"""

    users = """CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY NOT NULL,
        firstname character varying(50) NOT NULL,
        lastname  character varying(50) NOT NULL,
        othername character varying(50) NOT NULL,
        email  character varying(50) UNIQUE,
        phoneNumber numeric NOT NULL
        username character varying(50) NOT NULL,
        password character varying(50) NOT NULL,
        isAdmin boolean,
        registered timestamp default current_timestamp
    );"""

    meetups = """"CREATE TABLE IF NOT EXIST meetups(
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
        response character varying(30) NOT NULL,
    );"""

    tables =[users,meetups,questions,rsvps]

    return tables

#!/usr/bin/python
import psycopg2
import os


def _connect_to_db():
    #DATABASE_URL = os.environ['DATABASE_URL']
    DATABASE_URL = "postgres://nckviaogriuewz:96247ad5f30d86e18b45fbfe61a1b3f2d05c471074ad3c9c4804b8d3ad6bf708@ec2-54-225-227-125.compute-1.amazonaws.com:5432/dd8lle338hg0jh"

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # Define our connection string
    #conn_string = "host='localhost' dbname='postgres' user='postgres' password='Notredame1'"

    # print the connection string we will use to connect
    #print("Connecting to database\n	->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    #conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    print("Connected!\n")
    return conn


def get_by_date_time(date, time):
    conn = _connect_to_db()

    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM golf_board")

    # retrieve the records from the database
    records = cursor.fetchall()

    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    print(records)
    conn.close()


def add_to_db(name, score, rank, date, time):
    conn = _connect_to_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO golf_table (name, score, rank, date,time) VALUES (%s, %s, %s, %s, %s)',
                   (name, score, rank, date, time))

    conn.commit()
    conn.close()

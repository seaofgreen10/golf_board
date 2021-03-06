#!/usr/bin/python
import psycopg2
import logging
logger = logging.getLogger(__name__)

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
    cursor.execute('SELECT * FROM leaderboard WHERE date=%s AND time=%s', (date, time))

    # retrieve the records from the database
    records = cursor.fetchall()

    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    print(records)
    conn.close()


def add_score_to_db(name, score, today, thru, rank, date, time):
    conn = _connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO leaderboard (name, score, today, thru, rank, date, time) '
                       'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (name, score, today, thru, rank, date, time))
        logger.debug("Added row to db: %s %s" % (name, time))
    except psycopg2.Error as e:
        print("Exception caught in add_score_to_db:")
        print(e.pgerror)

    conn.commit()
    conn.close()


def swap_starter(to_start, to_bench):
    conn = _connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE public.roster '
                       'SET starting = true '
                       'WHERE golfer_name = \'%s\''%
                       to_start)
        cursor.execute('UPDATE public.roster '
                       'SET starting = false '
                       'WHERE golfer_name = \'%s\'' %
                       to_bench)
        logger.info('Swapping %s for %s' % (to_start, to_bench))
    except psycopg2.Error as e:
        print("Exception caught in swap_starter:")
        print(e.pgerror)

    conn.commit()
    conn.close()


def sign_golfer(to_add, team, starter, to_drop='none'):
    conn = _connect_to_db()
    cursor = conn.cursor()

    try:
        if to_drop != 'none':
            print(to_drop)
            cursor.execute('DELETE FROM public.roster '
                           'WHERE golfer_name = \'%s\'' % to_drop)

        starter_str = "false"
        if starter:
            starter_str = "true"
        cursor.execute('INSERT INTO public.roster '
                       '(golfer_name, team, starting)'
                       'VALUES (%s, %s, %s)',
                       (to_add, team, starter_str))
        logger.info('Adding %s, dropping %s, team %s' % (to_add, to_drop, team))
        conn.commit()
        conn.close()
    except psycopg2.Error as e:
        print("Exception caught in sign_golfer:")
        print(e.pgerror)


# return a list of all golfers by name from db (public.roster)
# param: flag to select starters only
def get_all_golfers(starters_only=False):
    conn = _connect_to_db()
    cursor = conn.cursor()

    try:
        query_str = 'SELECT golfer_name FROM public.roster'
        if starters_only:
            query_str += ' WHERE starting=\'true\''
        cursor.execute(query_str)
        records = cursor.fetchall()
    except psycopg2.Error as e:
        print("Exception caught in get_all_golfers:")
        print(e.pgerror)
        return 0

    names = []
    for record in records:
        names.append(record[0])
    return names


def increment_course_id():
    conn = _connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT value FROM public.general WHERE field=\'course_id\'')
        course = int(cursor.fetchone()[0])
        course += 1
        logger.info('Updating course id in database to %s' % str(course).zfill(3))
        cursor.execute('UPDATE public.general '
                       'SET value = \'%s\' '
                       'WHERE field = \'course_id\'' %
                       str(course).zfill(3))
        conn.commit()
        conn.close()
    except psycopg2.Error as e:
        print("Exception caught in increment_course_id:")
        print(e.pgerror)


def get_course_id():
    conn = _connect_to_db()
    cursor = conn.cursor()
    course = 0

    try:
        cursor.execute('SELECT value FROM public.general WHERE field=\'course_id\'')
        course = int(cursor.fetchone()[0])
    except psycopg2.Error as e:
        print("Exception caught in increment_course_id:")
        print(e.pgerror)

    return str(course).zfill(3)


def clear_leaderboard():
    conn = _connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM leaderboard')
        logger.info('Deleting all data from leaderboard')

        conn.commit()
        conn.close()
    except psycopg2.Error as e:
        print("Exception caught in clear_leaderboard:")
        print(e.pgerror)


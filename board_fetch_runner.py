import pgatour_site_2019_api_interface as api
import db_accessor as db
import datetime
import time
import logging
import signal
import sys


def sigterm_handler(signal, frame):
    # save the state here or do whatever you want
    print('shutting down')
    sys.exit(0)


signal.signal(signal.SIGTERM, sigterm_handler)


def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    logger.debug('helloworld')

    while True:
        # get today
        dt_today = datetime.datetime.today()
        course_id = db.get_course_id()

        # Sleep every 6 hours mon-wed
        if dt_today.weekday() < 3:  # 3=thursday
            logger.info('Not tournament day. Sleeping 6 hours')
            time.sleep(60*60*6)  # 60*60*6=6hrs
            if dt_today.weekday() == 1:  # 1=tuesday
                # Clear leaderboard on tuesday
                logger.info('Tuesday leaderboard cleanup')
                db.clear_leaderboard()
        else:
            list_of_players = db.get_all_golfers(True)
            # Check if tournament is in progress yet
            if api.is_in_progress() is False:
                # Not in progress, sleep for 2 hours
                logger.info('Tournament day, tournament not in progress. Sleeping 2 hours')
                time.sleep(60*60*2)  # 2hrs
            else:
                # Tournament in progress
                player_data_to_add = []
                logger.info('Tournament in progress. Going into tourney loop...')
                # while tournament is in progress, get score data for all players
                while api.get_players_data(course_id, str(dt_today.year), list_of_players, player_data_to_add):
                    print("data: " + str(player_data_to_add.__len__()))
                    # add all scores to db
                    for entry in player_data_to_add:
                        print("one entry")
                        db.add_score_to_db(entry.name,
                                           entry.score,
                                           entry.today,
                                           entry.thru,
                                           entry.rank,
                                           str(dt_today.date()),
                                           str(dt_today.time()))
                    # sleep 10 min
                    logger.info('Data added. Sleeping 10 min')
                    time.sleep(60*10)  # 10 min
                logger.debug('Round complete. Exited loop')
                time.sleep(60*60*8)  # 8hrs

        # end tournament - increment course key (in db)
        #db.increment_course_id()



main()


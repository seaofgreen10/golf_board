import pgatour_site_2019_api_interface as api
#import api_data_parser as parser
import db_accessor as db
import time
import pga_data.pga_scraper as pga
import datetime
import time


global year
global course


def main():
    ctr=0
    #out = pga.tourney('002', '2019')
    #print(out)
    #api.get_pga_data('002', '2019')

    #while(ctr<100):
    #    print("hi")
    #    ctr+=1
    #    time.sleep(10)


    # # if day isn't thursday-sunday, sleep 5 hours
    dt = datetime.datetime.today()

    #if True:
     #   return

    if datetime.datetime.today().weekday() < 3:  #3=thursday
        time.sleep(60*60*6)  # 60*60*6=6hrs
    # # else if tournament not in progress sleep 2 hours
    else:
        if api.is_in_progress(course, year) is False:
            time.sleep(60*60*2)  # 2hrs
        ## else while in progress, call api interface, sleep 10 min
        else:
            player_data_to_add = []
            while api.get_players_data(course, year, str(dt.date()), str(dt.time()), player_data_to_add):
                # add all scores to db
                for entry in player_data_to_add:
                    db.add_score_to_db(entry.name,
                                       entry.score,
                                       entry.today,
                                       entry.thru,
                                       entry.rank,
                                       str(dt.date()),
                                       str(dt.time()))
                # sleep 10 min
                time.sleep(60*10)  # 10 min


    ## end tournament - increment course key (in db)


    #db.add_to_db("nate", 20, 2, "2019-01-03", "00:00:00")
    #db.get_by_date_time("1", "2")
    #shutdown = 0
    #while not shutdown:
    #    data = api.get_leaderboard("json")
    #    parser.parse_json_data(data)


main()


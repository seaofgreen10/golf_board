#import api_interface.api_calls as api
#import api_interface.api_data_parser as parser
import db_accessor as db
import time

def main():
    ctr=0
    while(ctr<100):
        print("hi")
        ctr+=1
        time.sleep(10)

main()
#db.add_to_db("nate", 20, 2, "2019-01-03", "00:00:00")
#db.get_by_date_time("1", "2")
#shutdown = 0
#while not shutdown:
#    data = api.get_leaderboard("json")
#    parser.parse_json_data(data)



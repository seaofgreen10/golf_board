import api_calls as api
#import api_data_parser as parser
import db_accessor as db
import time
import pga_data.pga_scraper as pga

def main():
    ctr=0
    #out = pga.tourney('002', '2019')
    #print(out)
    api.get_pga_data('002', '2019')

    #while(ctr<100):
    #    print("hi")
    #    ctr+=1
    #    time.sleep(10)

main()



# # if day isn't thursday-sunday, sleep 5 hours
# # if tournament not in progress

# # else if hour (timezone) <10am   or >8pm, sleep 1 hour

## else kick off, sleep until ??




#db.add_to_db("nate", 20, 2, "2019-01-03", "00:00:00")
#db.get_by_date_time("1", "2")
#shutdown = 0
#while not shutdown:
#    data = api.get_leaderboard("json")
#    parser.parse_json_data(data)



import db_accessor as db
import json
import datetime

#input: array of names of players (first last)
#output: array of players with all relevant info
def extract_player_data(players_array):


def parse_json_data(date, time):
    #get list of players
    golfer_list = db.get_all_golfers()
    print(date)
    print(time)


    filename = "C:\\Users\\Pedro\\PycharmProjects\\pga_board\\api_interface\\output.txt"
    with open(filename, 'r') as myfile:
        json_data = myfile.read().replace('\n', '')

    parsed_json = json.loads(json_data)

    #for each player
    for golfer in golfer_list:
        golfer_str = str(golfer[0])
        #find entry
        for golfer_data in parsed_json['Players']:
            print('comparing %s to %s', (golfer_data['Name'].lower(), golfer_str.lower()))
            if golfer_data['Name'].lower() == golfer_str.lower():
                print('match')
                #get score
                score = golfer_data['TotalScore']
                rank = golfer_data['Rank']
                #add data to db
                print('would add %s %s %s %s %s', (golfer_str, score, rank, date, time))
                #db.add_score_to_db(name=golfer_str, score=score, rank=rank, date=date, time=time)
                break

nowd = datetime.datetime.now()
now = str(nowd)
parse_json_data(now.split()[0], now.split()[1])

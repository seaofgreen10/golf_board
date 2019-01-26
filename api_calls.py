import requests


def get_pga_data(course, year):
    url_str = 'https://statdata.pgatour.com/r/{}/{}/leaderboard-v2.json'.format(course, year)

    pga_json_data = requests.get(url_str).json()

    # For each player, in pga_json_data['leaderboard']['players'].__len__())
    for player in pga_json_data['leaderboard']['players']:
        print(player['player_bio']['first_name'])
        name = player['player_bio']['first_name'] + ' ' + player['player_bio']['last_name']



    #
    # print(pga_json_data['leaderboard']['players'].__len__())
    # print(pga_json_data['leaderboard']['players'][1]['player_bio']['first_name'])
    # print(pga_json_data['leaderboard']['players'][1]['player_bio']['last_name'])
    # print(pga_json_data['leaderboard']['players'][1]['current_position'])
    # print(pga_json_data['leaderboard']['players'][1]['thru'])
    # print(pga_json_data['leaderboard']['players'][1]['today'])
    # print(pga_json_data['leaderboard']['players'][1]['total'])
    #
    # print(pga_json_data['leaderboard']['start_date'])
    # print(pga_json_data['leaderboard']['end_date'])
    # print(pga_json_data['leaderboard']['is_started']) #true/fals
    # print(pga_json_data['leaderboard']['is_finished'])  # true/fals
    # print(pga_json_data['leaderboard']['current_round'])
    # print(pga_json_data['leaderboard']['round_state']) #In Progress, Official
    #
    # print(pga_json_data['leaderboard']['cut_line'])
    # print(pga_json_data['leaderboard']['cut_line']['cut_line_score'])





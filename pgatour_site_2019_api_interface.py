import requests
import collections
import logging
logger = logging.getLogger(__name__)
PlayerEntry = collections.namedtuple('PlayerEntry', 'name score today thru rank')


def _get_data_from_api(course='', year=''):
    # url_str = 'https://statdata.pgatour.com/r/{}/{}/leaderboard-v2.json'.format(course, year)
    url_str = 'https://statdata.pgatour.com/r/current/leaderboard-v2.json'
    return requests.get(url_str).json()


def get_players_data(course, year, list_of_players, player_data_to_add):
    # For each player, in pga_json_data['leaderboard']['players'].__len__())
    pga_json_data = _get_data_from_api(course, year)

    # check if we are still in progress
    if not is_in_progress():
        # if tournament is no longer in progress, break
        logger.info('Exiting as not in progress')
        return False

    for player in pga_json_data['leaderboard']['players']:
        name = player['player_bio']['first_name'] + ' ' + player['player_bio']['last_name']
        if name in list_of_players:
            score = player['total']
            today = player['today']
            thru = player['thru']
            rank = player['current_position']
            player_data_to_add.append(PlayerEntry(name=name, score=score, today=today, thru=thru, rank=rank))
            logger.info("added: " + str(player_data_to_add.__len__()))

    return True


def is_in_progress():
    pga_json_data = _get_data_from_api()
    if pga_json_data['leaderboard']['round_state'] == 'In Progress':
        return True
    else:
        return False


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





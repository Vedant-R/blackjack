def get_players(players):
    players_dict = {}
    for i in range(int(players)):
        players_dict[f'player_{i+1}'] = []
    return players_dict

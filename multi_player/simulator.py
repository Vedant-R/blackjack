from deck import deck
from hand import hand


def multiprocess_simulator(num_deck, num_players, batch, queue):

    player_list = []
    total_tie = 0
    total_dealer_won = 0

    for _ in range(0, batch):

        player_won, tie, dealer_won = hand(deck(num_deck), num_players)
        if not player_list:
            player_list = player_won
        else:
            for i, j in enumerate(player_won):
                player_list[i] += j
        total_tie += tie 
        total_dealer_won += dealer_won


    queue.put([player_list, total_tie, total_dealer_won])

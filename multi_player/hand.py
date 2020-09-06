import random
from players import get_players


def hand(new_deck, players=1):

    players_dict = get_players(players)

    dealer_hand = []
    win_list = [0] * players
    tie = 0
    dealer_won = 0

    random.shuffle(new_deck)

    for k, v in players_dict.items():
        v.append(new_deck.pop(0))

    dealer_hand.append(new_deck.pop(0))
    for k, v in players_dict.items():
        v.append(new_deck.pop(0))
    dealer_hand.append(new_deck.pop(0))

    for k, v in players_dict.items():
        while sum(v) < 17:
            v.append(new_deck.pop(0))

    d1 = players_dict.copy()
    for k, v in d1.items():
        k_idx = int(k.split('_')[1])
        while sum(dealer_hand) < sum(v):
            dealer_hand.append(new_deck.pop(0))

        if sum(v) > 21:
            dealer_won += 1

        if sum(dealer_hand) <= 21:
            if sum(v) <= 21:
                if sum(dealer_hand) == sum(v):
                    tie += 1
                elif sum(dealer_hand) > sum(v):
                    dealer_won += 1
                elif sum(dealer_hand) < sum(v):
                    win_list[k_idx-1] = 1

        if sum(dealer_hand) > 21:
            if sum(v) <= 21:
                win_list[k_idx-1] = 1
        
    return win_list, tie, dealer_won
   
import random


def hand(deck):
    '''Returns the result of a hand played

    Parameters:
    deck (list): a list of cards in deck

    Returns:
    int: score of the hand
    '''
    dealer_hand = []
    player_hand = []

    random.shuffle(deck)

    player_hand.append(deck.pop(0))
    dealer_hand.append(deck.pop(0))
    player_hand.append(deck.pop(0))
    dealer_hand.append(deck.pop(0))

    while sum(player_hand) < 17:
        player_hand.append(deck.pop(0))

    if sum(player_hand) > 21:
        return -1

    while sum(dealer_hand) < sum(player_hand):
        dealer_hand.append(deck.pop(0))

    if sum(dealer_hand) > 21:
        return 1

    if sum(player_hand) == sum(dealer_hand):
        return 0

    if sum(player_hand) > sum(dealer_hand):
        return 1

    if sum(player_hand) < sum(dealer_hand):
        return -1

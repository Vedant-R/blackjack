def deck(num_decks=1):
    '''Returns list of cards in deck/s
    
    Parameters:
    num_decks (int): number of decks (default 1)

    Returns
    list: list of cards in deck
    '''
    single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

    if num_decks == 0:
        raise ValueError("Deck cannot be 0!!!")
    return single_deck * num_decks

def deck(num_decks=1):

    single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

    if num_decks == 0:
        raise ValueError("Deck cannot be 0!!!")

    return single_deck * num_decks

from deck import deck
from hand import hand


def multiprocess_simulator(num_deck, batch, queue):
    '''Puts the results of hand in a queue

    Parameters:
    num_deck (int): total number of decks required
    batch (int): total number of batches to run
    queue (multiprocessing.queues.Queue): queue to put the hand results in
    '''
    player_won = 0
    tie = 0
    dealer_won = 0

    for _ in range(0, batch):

        outcome = hand(deck(num_deck))

        if outcome == 1:
            player_won += 1

        if outcome == 0:
            tie += 1

        if outcome == -1:
            dealer_won += 1

    queue.put([player_won, tie, dealer_won])

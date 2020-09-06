from multiprocessing import Queue, Process, cpu_count
import time

from simulator import multiprocess_simulator


def main(n_simulations, num_decks):
    '''Returns the result of scores after n simulations

    Parameters:
    n_simulations (int): the total number of simulations
    num_decks (int): the total number of decks

    Returns:
    str: A multiline string with the stats of the simulation and scores
    '''
    start = time.time()

    batch = int(n_simulations / cpu_count()) + (n_simulations % cpu_count() > 0)
    queue = Queue()

    all_processes = []
    for _ in range(0, cpu_count()):
        process = Process(target=multiprocess_simulator, args=(num_decks, batch, queue))
        all_processes.append(process)
        process.start()

    for proc in all_processes:
        proc.join()

    end = time.time() - start

    player_won = 0
    tie = 0
    dealer_won = 0

    for _ in range(0, cpu_count()):
        outcome = queue.get()
        player_won += outcome[0]
        tie += outcome[1]
        dealer_won += outcome[2]

    return f"""
    {cpu_count()} CPU cores utilised.
    The simulator ran {n_simulations} times.
    The player won {player_won} times.
    The dealer won {dealer_won} times.
    There were {tie} draws.
    The execution took {round(end, 2)} seconds.
    """


if __name__ == "__main__":
    print("Enter number of simulations (int > 0): ")
    n_simulations = int(input())
    print("Enter number of decks (int > 0): ")
    num_decks = int(input())
    print("\n=============== Results ================")
    print(main(n_simulations, num_decks))
    print("==========================================")

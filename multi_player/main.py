from multiprocessing import Queue, Process, cpu_count
import time

from simulator import multiprocess_simulator


def main(n_simulations, num_decks, num_players):
    start = time.time()

    batch = int(n_simulations / cpu_count()) + (n_simulations % cpu_count() > 0)
    queue = Queue()

    all_processes = []
    for _ in range(0, cpu_count()):
        process = Process(target=multiprocess_simulator, args=(num_decks, num_players, batch, queue))
        all_processes.append(process)
        process.start()

    for proc in all_processes:
        proc.join()

    end = time.time() - start

    player_won = []
    tie = 0
    dealer_won = 0

    outcome = queue.get()
    if not player_won:
        player_won = outcome[0]
    else:
        for i, j in enumerate(outcome[0]):
            player_won[i] += j
    tie += outcome[1]
    dealer_won += outcome[2]

    player_won_string = ''''''
    for i, j in enumerate(player_won):
        player_won_string += f"Player{i+1} won {j} times. "

    return f"""
    {cpu_count()} CPU cores utilised.
    The simulator ran {n_simulations} times.
    {player_won_string}
    The dealer won {dealer_won} times.
    There were {tie} draws.
    The execution took {round(end, 2)} seconds.
    """


if __name__ == "__main__":
    print("Enter number of simulations (int > 0): ")
    n_simulations = int(input())
    print("Enter number of decks (int > 0): ")
    num_decks = int(input())
    print("Enter number of players (int > 0): ")
    num_players = int(input()) 
    print("\n=============== Results ================")
    print(main(n_simulations, num_decks, num_players))
    print("==========================================")

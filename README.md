# Blackjack Monte Carlo Simulation

This work focusses on a Monte Carlo simulator for a cut down version of
Blackjack.

The simulator follows these rules:

- The player takes all his turns first and then the dealer afterwards.

- The player will automatically hit (take another card) if the total they have is less than 17, otherwise they will stand (stick with the cards they have). The player could hit multiple times.

- If the player hits and goes bust, then the dealer will win.

- If the player has the same value as the dealer then it’s a draw.

- If the player has more than the dealer, then the dealer will hit. The dealer could hit multiple times.
- Assume an Ace as 11 to make life easy.

- Other rules of Blackjack are ignored, such splitting when a person receives a pair, as we want to keep this simple.

- Simulator should be runnable for N number of simulations

The output of the simulation should be:

```shell
“The simulator ran N times
The player won _ times
The dealer won _ times
There were _ draws”
```

## Requirements

- Python3

- `pip install -r requirements.txt`

## Explanation

This work is divided into 2 parts.

- Part 1

[Single Player Game](single_player)

- Part 2

[Multi Player Game](multi_player) (I have given a shot for multiplayer version as well, this works for single as well as multi).
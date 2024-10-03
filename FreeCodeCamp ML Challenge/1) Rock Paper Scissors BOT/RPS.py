# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
import random
from collections import Counter


def playerold(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess


def player(prev_play, player1, player2, opponent_history=[],play_order = [{"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}]):
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    if player2 is kris:
        if prev_play == '':
            prev_play = 'S'
        return prev_play
        prev_play = ideal_response[ideal_reponse[prev_play]]
    if player2 is abbey:
        if not prev_play:
            prev_play = 'R'
        opponent_history.append(prev_play)
        last_two = "".join(opponent_history[-2:])
        if len(last_two) == 2:
            play_order[0][last_two] += 1
        potential_plays = [prev_play + "R", prev_play + "P",prev_play + "S"]
        sub_order = {k: play_order[0][k]
            for k in potential_plays if k in play_order[0]}
        prediction = max(sub_order, key=sub_order.get)[-1:]
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response[ideal_response[prediction]]
    else:
        if prev_play == '':
            prev_play = "R"
        return ideal_response[prev_play]
        
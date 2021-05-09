from game import constants as game_constants
import random


def get_random_number(array):
    random_move = random.choice(array)
    return random_move


def is_game_over(game_instance):
    # import ipdb; ipdb.set_trace()
    # Horizontal
    if game_instance.q1 == game_instance.q2 and game_instance.q2 == game_instance.q3:
        if game_instance.q1 != game_constants.DRAW:
            return game_instance.q1
    if game_instance.q4 == game_instance.q5 and game_instance.q5 == game_instance.q6:
        if game_instance.q4 != game_constants.DRAW:
            return game_instance.q4
    if game_instance.q7 == game_instance.q8 and game_instance.q8 == game_instance.q9:
        if game_instance.q7 != game_constants.DRAW:
            return game_instance.q7

    # Vertical
    if game_instance.q1 == game_instance.q4 and game_instance.q4 == game_instance.q7:
        if game_instance.q1 != game_constants.DRAW:
            return game_instance.q1

    if game_instance.q2 == game_instance.q5 and game_instance.q5 == game_instance.q8:
        if game_instance.q2 != game_constants.DRAW:
            return game_instance.q2

    if game_instance.q3 == game_instance.q6 and game_instance.q6 == game_instance.q9:
        if game_instance.q3 != game_constants.DRAW:
            return game_instance.q3

    # Diagonal
    if (
        game_instance.q1 == game_instance.q5 and game_instance.q5 == game_instance.q9
    ) or (
        game_instance.q3 == game_instance.q5 and game_instance.q5 == game_instance.q7
    ):
        if game_instance.q5 != game_constants.DRAW:
            return game_instance.q5

    return None

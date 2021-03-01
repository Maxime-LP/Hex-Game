from random import choice
from AI.mean.best_action_average import best_action_average

def run_random(board, color):
    i, j = board.action_to_coord(choice(board.actions))
    return i, j


def run_mean(board, color):
    n = 10
    
    best_action = best_action_average(board, n, color)
    i, j = board.action_to_coord(best_action)
    return i, j


def run_ucb1(board):
    return


def run_mcts(board):
    """
    Jouer N=100 parties sur chaque case libre et voir quelle case a le meilleur score
    Y-a-t-il une meilleure valeur de N ? On peut augmenter la valeur de N à chaque coup car moins de cases à tester
    """
    return
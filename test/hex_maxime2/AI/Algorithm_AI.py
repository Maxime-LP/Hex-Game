from random import choice
from AI.mean.best_action import best_action

def run_random(board, color):
    i, j = board.action_to_coord(choice(board.actions))
    return i, j

def run_mean(board, color):
    """
    Jouer N parties sur chaque case libre et voir quelle case a le meilleur score
    Y-a-t-il une meilleure valeur de N ? On peut augmenter la valeur de N à chaque coup car moins de cases à tester
    """
    # if x = 10000, it is equivalent to test 100 games/play
    x = 1000
    n = int(x / (board.size**2 + len(board.actions)))
    action = best_action(board, n, color)
    return board.action_to_coord(action)

def run_ucb1(board):
    return

def run_mcts(board):
    return
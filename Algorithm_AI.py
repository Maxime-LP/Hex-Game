from random import choice

def run_random(board):
    i, j = board.action_to_coord(choice(board.actions))
    return i, j

def run_ucb1(board):
    return

def run_mcts(board):
    """
    Jouer N=100 parties sur chaque case libre et voir quelle case a le meilleur score
    Y-a-t-il une meilleure valeur de N ? On peut augmenter la valeur de N à chaque coup car moins de cases à tester
    """
    return
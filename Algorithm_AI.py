from random import choice

def run_random(board):
    i, j = board.action_to_coord(choice(board.actions))
    return i, j

def run_ucb1(board):
    return

def run_mcts(board):
    return
import numpy.random as npr

def run_random(board):
    while True:
        i = npr.randint(0, board.size)
        j = npr.randint(0, board.size)
        if board.board[i,j] == 0:
            return i, j

def run_ucb1(board):
    return

def run_mcts(board):
    return
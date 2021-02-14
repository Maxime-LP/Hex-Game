from random import randint

def run_random(board):
    while True:
        i = randint(0, board.size-1)
        j = randint(0, board.size-1)
        if board.board[i][j] == 0:
            return i, j

def run_ucb1(board):
    return

def run_mcts(board):
    return
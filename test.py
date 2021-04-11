import numpy as np
import matplotlib.pyplot as plt
from Board import Board
from Game import Game
from Player import Human, AI



def test(testType,player1Type,player2Type,board_size):
    ai_algorithms = ['random', 'mc0', 'mc', 'mc_ucb1', 'mcts']

    if player1Type not in ai_algorithms:
        raise Exception("Wrong player 1 type ")
    if player2Type not in ai_algorithms:
        raise Exception("Wrong player 2 type")
    
    if testType == 'test1':
        RED, BLUE = 1, 2
        player1 = AI(RED, player1Type)
        player2 = AI(BLUE, player2Type)
        test1(player1,player2,board_size)

    elif testType == 'test2':
        pass


def test1(player1,player2,board_size,n=10):

    C = np.linspace(0,2,10)
    res = []
    for explorationConstant in C:
        print(explorationConstant)
        blueWinrate = 0
        for i in range(n):
            board = Board(board_size)
            game = Game(board, player1, player2)
            blueWinrate += game.runNoDisplay(explorationConstant)

        res.append(blueWinrate/n)

    plt.bar(C,res)
    plt.show()

def test2():
    pass
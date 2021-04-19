#!/usr/bin/env python3
import sys
import os
from time import time
import numpy as np
from multiprocessing import Pool
import matplotlib.pyplot as plt
from Board import Board
from Game import Game
from Player import AI


def test(args):
    n,c = args
    # settings
    RED, BLUE = 1, 2
    ai_algorithms = ['random', 'mc', 'mc_ucb1', 'uct']
    player1_type, player2_type, board_size, test_type = sys.argv[1:]
    
    # init red player
    if player1_type in ai_algorithms:
        player1 = AI(RED, player1_type)
    else:
        raise TypeError("Wrong player 1 type ")

    # init blue player
    if player2_type  in ai_algorithms:
        player2 = AI(BLUE, player2_type)
    else:
        raise Exception("Wrong player 2 type")

    return test1(player1, player2, board_size, n, c)
  

def test1(player1, player2, board_size, n, c):
    if c != None:
        player2.explorationConstant = c
    board = Board(board_size)
    game = Game(board, player1, player2)
    winner = game.runNoDisplay()
    return winner

if __name__ == "__main__":

    start_time = time()
    n = 10

    cst_list = list(np.linspace(0,0.5,3))

    result = []
    for c in cst_list:
        p = Pool(processes=os.cpu_count())
        win_rate = p.map(test, [[n, c]]*n)
        result.append(np.mean(win_rate))

    exe_time = time() - start_time    
    print(f'{round(n*len(cst_list)/exe_time,3)} games/s in {round(exe_time,3)}s.')
    print(f'Win rate(s): {result}')


#!/usr/bin/env python3
import sys
import os
from time import time
import numpy as np
from multiprocessing import Pool

from Board import Board
from Game import Game
from Player import AI


def progressbar(it, prefix="Computing: ", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def test(args):
    #n, c = args
    # settings
    RED, BLUE = 1, 2
    ai_algorithms = ['random', 'mc', 'mc_ucb1', 'uct']
    player1_type, player2_type, board_size, n = sys.argv[1:]
    
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

    return test1(player1, player2, board_size, *args)
  

def test1(player1, player2, board_size, n, c):
    if c != None:
        player2.explorationConstant = c
    board = Board(board_size)
    game = Game(board, player1, player2)
    winner = game.runNoDisplay()
    return winner


if __name__ == "__main__":
    
    start_time = time()
    
    n = int(sys.argv[4])
    cst_list = list(np.linspace(0,0.5,21))

    result = []
    for c in progressbar(cst_list):
        p = Pool(processes=os.cpu_count())
        win_rate = p.map(test, [[n, c]]*n)
        result.append(np.mean(win_rate))

    exe_time = time() - start_time    
    print(f'{round(n*len(cst_list)/exe_time,3)} games/s in {round(exe_time,3)}s.')
    print(f'List explorationConstant: {cst_list}')
    print(f'Win rate(s): {result}')


#!/usr/bin/env python3
import sys
import os
from time import time
from tqdm import tqdm
import numpy as np
from multiprocessing import Pool

from Board import Board
from Game import Game
from Player import AI


def test(args):
    c, n = args 
    # settings
    RED, BLUE = 1, 2
    ai_algorithms = ['random', 'mc', 'mc_ucb1', 'uct', 'uct_wm']
    player1_type, player2_type, board_size = sys.argv[1:4]
    
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

    if c != None:
        player2.explorationConstant = c

    board = Board(board_size)
    game = Game(board, player1, player2)
    winner = game.runNoDisplay()
    
    return winner


if __name__ == "__main__":

    start_time = time()
    
    n = int(sys.argv[4])
    cst_list = [0.3] #np.round(list(np.linspace(0,4,21)),3)
    result = []
    
    for c in tqdm(cst_list):
        leave = True if len(cst_list) <= 1 else False
        with Pool(processes=os.cpu_count()) as p:
            win_rate = list(tqdm(p.imap(test, [[c,1]]*n), total=n, leave=leave))
            #result.append(np.mean(win_rate))

    exe_time = time() - start_time

    try:
        k = 1
        if sys.argv[5] == 'save':
            with open("simulations_rapport/logs.py", "a") as filout:
                filout.write(f'# {sys.argv[1]} vs {sys.argv[2]} on {n} games and n=1000\n')
                filout.write(f'win_rate_ = {win_rate}\n\n')
    except IndexError:
        
        print(f'{n*len(cst_list)} games in {round(exe_time,3)}s => {round(n*len(cst_list)/exe_time,3)} games/s')
        print(f'List explorationConstant: {cst_list}')
        print(f'Win rate(s): {np.round(result,4)}')

#!/usr/bin/env python3
import sys
import os
from time import time
from multiprocessing import Process, Queue
import numpy as np
import matplotlib.pyplot as plt
from Board import Board
from Game import Game
from Player import AI


def test(queue, player1_type, player2_type, board_size, test_type, n, cst_list):
    # init red player
    RED, BLUE = 1, 2
    ai_algorithms = ['random', 'mc', 'mc_ucb1', 'mcts']
    if player1_type in ai_algorithms:
        player1 = AI(RED, player1_type)
    else:
        raise TypeError("Wrong player 1 type ")

    # init blue player
    if player2_type  in ai_algorithms:
        player2 = AI(BLUE, player2_type)
    else:
        raise Exception("Wrong player 2 type")

    # selects a test
    tests = {'test1': best_explor_cst,
             'test2': who_is_the_best}
    make_test = tests[test_type]
    make_test(queue, player1, player2, board_size, n, cst_list)


def best_explor_cst(queue, player1, player2, board_size, n, cst_list):

    mcts_winrate_per_cst = []

    if player2.algorithm.__name__ != 'mcts':
        raise Exception("Player 2 type must be mcts for test1.")

    for explorationConstant in cst_list:
        player2.explorationConstant = explorationConstant
        mcts_winrate = 0
        for i in range(n):
            board = Board(board_size)
            game = Game(board, player1, player2)
            mcts_winrate += game.runNoDisplay()
        mcts_winrate_per_cst.append(mcts_winrate / n)
    
    queue.put(mcts_winrate_per_cst)
    

def who_is_the_best(queue, player1, player2, board_size, n, C=None):
    w = 0
    for i in progressbar(range(n), "Computing: ", 40):
        board = Board(board_size)
        game = Game(board, player1, player2)
        w += game.runNoDisplay()
    winrate = w / n
    queue.put([winrate])

def progressbar(it, prefix="", size=60, file=sys.stdout):
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

if __name__ == "__main__":

    player1_type = sys.argv[1]
    player2_type = sys.argv[2]
    board_size = sys.argv[3]
    test_type = sys.argv[5]
    # number of simulations
    n = 1000
    # exploration constants for mcts
    cst_list = np.linspace(0, .5, 20)

    num_processes = 50 #os.cpu_count()
    if n // num_processes == 0:
        print("Tips: use a divisor of n to increase speed.")
        #raise Exception('# of processes should divide # of games n.')
    d, r = n//num_processes, n%num_processes
    nb_games = [d] * (num_processes-1) + [d+r] # nb of simulated games per process

    queue = Queue()

    processes = []
    for i in range(num_processes):
        process = Process(target=test,
                          args=(queue, 
                                player1_type,
                                player2_type,
                                board_size,
                                test_type,
                                nb_games[i],
                                cst_list))
        processes.append(process)

    print(f'# CPU: {os.cpu_count()}')
    print(f'# processes: {num_processes}')
    print(f'# games per process: {nb_games}.')

    time0 = time() 
    
    for process in processes:
        process.start()

    for process in progressbar(processes, "Computing: ", 40):
        process.join()

    winrates = np.empty(shape=(0,len(cst_list)))
    while not queue.empty():
        winrates = np.append(winrates, [queue.get()], axis=0)

    res = []
    for col in winrates.T:
        res.append(np.mean(col))

    print(f'Blue player winrate: {res}.')
    print(f'-> {round(n / (time()-time0),2)} games/s with {num_processes} processes.')

    if test_type == "test1":
        plt.plot(cst_list, res, marker='o')
        plt.xlabel("Exploration constant")#, size = 16)
        plt.ylabel("Winrate")#, size = 16)
        plt.title(f"UCT's winrate on {n} games vs {player1_type}") 
              #fontdict={'color' : 'darkblue',
                #        'size': 14})
        plt.savefig(f"simulations/{time()}.png")

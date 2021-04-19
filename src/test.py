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
    ai_algorithms = ['random', 'mc', 'mc_ucb1', 'uct']
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

    if player2.algorithm.__name__ not in ['mc_ucb1', 'uct']:
        raise Exception("Player 2 type must be mc_ucb1 or uct for test1.")

    for explorationConstant in cst_list: #progressbar(cst_list, "Computing: ", 40):
        print(explorationConstant)
        player2.explorationConstant = explorationConstant
        mcts_winrate = 0
        for i in progressbar(range(n), "Computing: ", 40):
            board = Board(board_size)
            game = Game(board, player1, player2)
            mcts_winrate += game.runNoDisplay()
        mcts_winrate_per_cst.append(mcts_winrate / n)
    
    queue.put(mcts_winrate_per_cst)
    

def who_is_the_best(queue, player1, player2, board_size, n, cst_list=None):
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
    '''
    player1_type = sys.argv[1]
    player2_type = sys.argv[2]
    board_size = sys.argv[3]
    test_type = sys.argv[4]
    '''
    print(type(sys.argv))
    player1_type,player2_type,board_size,test_type = sys.argv[1:]
    # number of simulations
    total_games = 500
    # exploration constants for mcts
    cst_list = [None]#np.linspace(0,0.5,11)

    num_processes = 50 #os.cpu_count()
    if total_games // num_processes == 0:
        print("Tips: use a divisor of n to increase speed.")
        #raise Exception('# of processes should divide # of games n.')
    d, r = total_games // num_processes, total_games % num_processes
    games_per_process = [d] * (num_processes-1) + [d+r]

    queue = Queue()

    processes = []
    for i in range(num_processes):
        process = Process(target=test,
                          args=(queue, 
                                player1_type,
                                player2_type,
                                board_size,
                                test_type,
                                games_per_process[i],
                                cst_list))
        processes.append(process)

    print(f'# CPU: {os.cpu_count()}')
    print(f'# processes: {num_processes}')
    print(f'# games per process: {games_per_process}.')

    time0 = time() 
    
    for process in processes:
        process.start()

    for process in processes:
        process.join()

    winrates = np.empty(shape=(0,len(cst_list)))
    while not queue.empty():
        winrates = np.append(winrates, [queue.get()], axis=0)

    res = []
    for col in winrates.T:
        res.append(np.mean(col))

    print(f'Blue player winrate: {res}.')
    print(f'{round(total_games * len(cst_list) / (time()-time0),2)} games/s with {num_processes} processes.')
    print(f'Execution time: {round(time()-time0,2)}s')
    
    if test_type == "test1":
        plt.plot(cst_list, res, marker='o')
        plt.xlabel("Exploration constant")
        plt.ylabel("Win rate")
        plt.title(f"UCT's win rate on {total_games} games vs UCT")
        plt.savefig(f"simulations/{time()}.png")

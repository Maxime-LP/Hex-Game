#!/usr/bin/env python3
import sys
import os
from time import time
from multiprocessing import Process
import numpy as np
import matplotlib.pyplot as plt
from Board import Board
from Game import Game
from Player import AI


def test(testType, player1_type, player2_type, board_size, n=10):
    RED, BLUE = 1, 2
    ai_algorithms = ['random', 'mc', 'mc_ucb1', 'mcts']
    # init red player
    if player1_type in ai_algorithms:
        player1 = AI(RED, player1_type)
    else:
        raise Exception("Wrong player 1 type ")
    # init blue player
    if player2_type  in ai_algorithms:
        player2 = AI(BLUE, player2_type)
    else:
        raise Exception("Wrong player 2 type")
    # selects a test
    tests = {'test1': test1,
             'test2': test2}
    make_test = tests[sys.argv[5]]
    make_test(player1, player2, board_size, n)


def test1(player1, player2, board_size, n):
    print('Simulations in progress...')
    time0 = time()
    RED, BLUE = 1, 2
    C = np.linspace(0.05,1,5)
    res = []
    if player2.algorithm.__name__ != 'mcts':
        raise Exception("Player 2 type must be mcts for test1.")

    for explorationConstant in C:
        print('\nexplor_cst:', explorationConstant)
        player2.explorationConstant = explorationConstant
        mcts_winrate = 0
        for i in range(n):
            print(i)
            board = Board(board_size)
            game = Game(board, player1, player2)
            mcts_winrate += game.runNoDisplay()
        res.append(mcts_winrate / n)

    print(f'Execution : {time()-time0}s')

    plt.plot(C, res, marker='o')
    plt.xlabel("Exploration constant", size = 16,)
    plt.ylabel("Winrate", size = 16)
    plt.title(f"UCT's winrate on {n} games vs {player1.algorithm.__name__}", 
          fontdict={'color' : 'darkblue',
                    'size': 14})
    plt.savefig(f"simulations/{time()}.png")
    

def test2(player1, player2, board_size, n):
    #print('Simulations in progress...')
    time0 = time()
    w = 0
    for i in range(n):
        board = Board(board_size)
        game = Game(board, player1, player2)
        w += game.runNoDisplay()

    if __name__!='__main__':
        print(f'Win rate Blue: {w/n}')
        t = time()-time0
        print(f'{round(n/t,3)} games/s - {round(n*60/t,3)} games/min')
        print(f'Time for {n} games: {round(t,3)}s')
    

if __name__ == "__main__":
    player1_type = sys.argv[1]
    player2_type = sys.argv[2]
    board_size = sys.argv[3]
    testType = sys.argv[5]
    n = 100
    for num_processes in range(50,51):
        processes = []
        #num_processes = os.cpu_count()
        # Use os.cpu_count() to obtain num CPU
        d, r = n//num_processes, n%num_processes
        nb_games = [d] * (num_processes-1) + [d+r]
        for i in range(num_processes):
            process = Process(target=test,
                              args=(testType,
                                    player1_type,
                                    player2_type,
                                    board_size,
                                    nb_games[i]))
            processes.append(process)

        print('Simulations in progress...')
        print(f'# CPU: {os.cpu_count()}')
        print(f'# processes: {num_processes}')
        print(f'# games per process: {nb_games}.')

        time0 = time()

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print(f'-> Time for {n} games: {round(time()-time0,2)}s with {num_processes} processes.\n')


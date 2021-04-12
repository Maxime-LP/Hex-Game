#!/usr/bin/env python3
import sys
from time import time
from math import sqrt
import colorama # translate ANSI sequence for Windows
colorama.init()

from misc import display
if display:
    import pygame
    from misc import screen, background
    from Player import Human
from Game import Game
from Player import AI
from Board import Board
from test import test


####### Init Game, Players and Board instances #######

#init boardgame
board_size = sys.argv[3]
board = Board(board_size)

#init players
RED, BLUE = 1, 2
ai_algorithms = ['random', 'mc0', 'mc', 'mc_ucb1', 'mcts']

if sys.argv[1] == 'h' and display:   # h for human
    player1 = Human(RED)
elif sys.argv[1] in ai_algorithms:
    player1 = AI(RED, sys.argv[1])
else:
    print(f'Wrong player type. Available options: {["h"] + ai_algorithms}.')
    exit()

if sys.argv[2] == 'h' and display:
    player2 = Human(BLUE)
elif sys.argv[2] in ai_algorithms:
    player2 = AI(BLUE, sys.argv[2])
else:
    print(f'Wrong player type. Available options: {["h"] + ai_algorithms}.')
    print("Don't use 'h' player with no display.")
    exit()

#####################################################


# Let's play ####################

if display:
    game = Game(board, player1, player2)
    pygame.init()
    pygame.display.set_caption("Hex")
    screen.blit(background,(0,0))
    game.run()

elif (not display) and sys.argv[1] in ai_algorithms and sys.argv[2] in ai_algorithms:
    print('...')
    time0 = time()
    n = 100
    w = 0
    for i in range(n):
        #print(i)
        board = Board(board_size)
        game = Game(board, player1, player2)
        w += game.runNoDisplay()    
    print(f'#games = {n}')
    print(f'Win rate Blue: {w/n}')
    t = round(time()-time0, 4)
    print(f'Time for {n} games:', t)
    print(f'{n / t} games/s')
    print(f'{n*60 / t} games/min')

if sys.argv[4] == 'test1':
    test('test1',sys.argv[1],sys.argv[2],board_size)

elif (sys.argv[1]=='h') | (sys.argv[2]=='h'):
    print('Players must be AI.')


#####################################################



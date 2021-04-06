#!/usr/bin/env python3
import sys
from time import time
import pygame
from misc import board_size, screen, background
from Game import Game
from Player import Human, AI
from Board import Board
import colorama # translate ANSI sequence for Windows
colorama.init()

"""
CONTROLS
ESC : Quit the game
"""

####### Init Game, Players and Board instances #######

#init boardgame
board = Board(board_size)

#init players
RED, BLUE = 1, 2
ai_algorithms = ['random', 'mc0', 'mc', 'mcts']

if sys.argv[1] == 'h':   # h for human
    player1 = Human(RED)
elif sys.argv[1] in ai_algorithms:
    player1 = AI(RED, sys.argv[1])
else:
    print(f'Veuilliez saisir un type de joueur correct : {["h"] + ai_algorithms}.')
    exit()

if sys.argv[2] == 'h':
    player2 = Human(BLUE)
elif sys.argv[2] in ai_algorithms:
    player2 = AI(BLUE, sys.argv[2])
else:
    print(f'Veuilliez saisir un type de joueur correct : {["h"] + ai_algorithms}.')
    exit()


#init game
game = Game(board, player1, player2)

#####################################################


# Let's play ####################

if sys.argv[4]=='1':
    pygame.init()
    pygame.display.set_caption("Hex")
    screen.blit(background,(0,0))
    game.run()

elif sys.argv[4]=='0' and sys.argv[1] in ai_algorithms and sys.argv[2] in ai_algorithms:
    time0 = time()
    n = 1000
    w = 0
    for i in range(n):
        board = Board(board_size)
        game = Game(board, player1, player2)
        w += game.runNoDisplay()
    print(f'#games = {n}')
    print(f'Win rate Blue: {w/n}')
    print(f'{round(n/(time()-time0), 4)} games/s')

elif (sys.argv[1]=='h') | (sys.argv[2]=='h'):
    print('Players must be AI.')

#####################################################

#!/usr/bin/env python3
import sys
import pygame
from misc import board_size, screen, background
from time import time
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

if sys.argv[1] == '0':
    player1 = Human(RED)
elif sys.argv[1] == '1':
    player1 = AI(RED, 'random')
else:
    print('Veuilliez saisir un type de joueur correct : 0 ou 1.')
    exit()

if sys.argv[2] == '0':
    player2 = Human(BLUE)
elif sys.argv[2] == '1':
    player2 = AI(BLUE, 'random')
else:
    print('Veuilliez saisir un type de joueur correct : 0 ou 1.')
    exit()


#init game
game = Game(board, player1, player2)

#####################################################


# Let's play ####################

if sys.argv[4]=='1':
    pygame.init()
    pygame.display.set_caption("Hex")
    #apply boardgame picture
    screen.blit(background,(0,0))
    game.run()

elif sys.argv[4]=='0' and sys.argv[1]=='1' and sys.argv[2]=='1':
    time0 = time()
    n = 10000
    w = 0
    for i in range(n):
        board = Board(board_size)
        game = Game(board, player1, player2)
        w += game.runNoDisplay()
    print(f'Win rate Blue: {w/n}')
    print(f'{round(n/(time()-time0), 4)} games/s')

elif (sys.argv[1]=='0') | (sys.argv[2]=='0'):
    print('Players must be AI.')

#####################################################

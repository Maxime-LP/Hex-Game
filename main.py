#!/usr/bin/env python3
import sys
import pygame
from Game import Game
from Player import Human, AI
from Board import Board

"""
Description du fichier
"""


############### Init graphical window ################

board_size = sys.argv[3]

pygame.init()
screen = pygame.display.set_mode((1300,900))
background = pygame.image.load(f"img/Hex_board_{board_size}.png")
pygame.display.set_caption("Hex")

#   0__________________x=1300
#   |
#   | (x0,y0)
#   |  
#   |       screen
#   |
#   y=900

#apply boardgame picture
screen.blit(background,(0,0))

#####################################################



####### Init Game, Player and Board instances #######

#init boardgame
board = Board(board_size, background, screen)

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


##################### Let's play ####################

game.run()

#####################################################
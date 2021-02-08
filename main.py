#!/usr/bin/env python3
import sys
import pygame
from Game import Game
from Player import Player
from Board import Board


##### Initialisations de la fenêtre graphique #####
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

#appliquer l'image du plateau de jeu
screen.blit(background,(0,0))

##### Initialisation des instances Game, Player #####

#init boardgame
board = Board(board_size, background, screen)

player1 = Player(int(sys.argv[1]), 'red', board.board)
player2 = Player(int(sys.argv[2]), 'blue', board.board)

#init game
game = Game(board, player1, player2)


##### Boucle principale #####
game.run()
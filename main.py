#!/usr/bin/env python3
import sys
import pygame
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


############### Init window ################

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



####### Init Game, Players and Board instances #######

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

"""
###loop 

def loop(n=1):
    #Plays n games and counts the number of times blue wins

    t0=time()
    res = 0
    for i in range(n):
        res += game.run() - 1
        game.reset()

    print("Nb of game :", n)
    print(f"Win rate (2nd player): {round(res/n*100, 2)}%")
    t = round(time()-t0,4)
    print(f"Tps d'éxécution : {t}s")
    print("Games/s :", round(n/t,2))

try:
    loop(int(sys.argv[4]))
except IndexError:
    loop()
except ValueError:
    print("Please enter an integer to define the number of games.")
    """
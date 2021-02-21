#!/usr/bin/env python3
import sys
from time import time
from Game import Game
from Player import Human, AI
from Board import Board
# translate ANSI sequence for Windows
import colorama

colorama.init()

t0 = time()


####### Init Game, Players and Board instances #######

#init boardgame
board = Board(int(sys.argv[3]))

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

n = 10000

res = 0
for i in range(n):
    res += game.run() - 1
    game.reset()

print(f"Le second joueur à remporté {res/n*100}% des parties.")
print(f"Tps d'éxécution : {time()-t0}s")

#####################################################
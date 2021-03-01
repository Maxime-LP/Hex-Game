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
    player1 = AI(RED, 'mean')
else:
    print('Please enter a correct player type : 0 or 1.')
    exit()

if sys.argv[2] == '0':
    player2 = Human(BLUE)
elif sys.argv[2] == '1':
    player2 = AI(BLUE, 'mean')
else:
    print('Please enter a correct player type : 0 or 1.')
    exit()


#init game
game = Game(board, player1, player2)

#####################################################


##################### Let's play ####################
game.run()
'''
def loop(n=1):
    """
    Play n game. Build for AI player.
    """
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
'''
#####################################################
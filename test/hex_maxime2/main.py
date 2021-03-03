#!/usr/bin/env python3
import sys
from time import time
t0 = time()
from Game import Game
from Player import AI
from Board import Board

# translate ANSI sequence for Windows
import colorama
colorama.init()

####### Init Game, Players and Board instances #######

#init boardgame
board = Board(int(sys.argv[1]))

#init players
RED, BLUE = 1, 2
player1 = AI(RED, 'mean')
player2 = AI(BLUE, 'random')

#init game
game = Game(board, player1, player2)

#####################################################


##################### Let's play ####################

game.run()

def loop(n=1):
    """
    Play n game. Build for AI player.
    """
    res = 0
    for i in range(n):
        game.reset()
        res += game.run() - 1
        print(i)

    print("Nb of game :", n)
    print(f"Win rate (2nd player): {round(res/n*100, 2)}%")
    t = round(time()-t0,4)
    print(f"Tps d'éxécution : {t}s")
    print("Games/s :", round(n/t,2))

try:
    loop(int(sys.argv[2]))
except IndexError:
    loop()
except ValueError:
    print("Please enter an integer to define the number of games.")

#####################################################
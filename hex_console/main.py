#!/usr/bin/env python3

import sys
import re
from Player import Player
from Board import Board
from Game import Game


#stone's color
color = {1:"\033[34m⬢ \033[0m", 2:"\033[31m⬢ \033[0m"} # 1:blue and 2:red

#init players
player1 = Player('Player 1', color[1])
player2 = Player('Player 2', color[2])

#init boardgame
board = Board()

#init game
game = Game(board, player1, player2)

# Let's play!
game.play()
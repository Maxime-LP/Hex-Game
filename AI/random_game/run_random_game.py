#!/usr/bin/env python3
from Game import Game
from Player import AI
from Board import Board

def loop(n=1):
    """
    Play n game. Build for AI player.
    """
    res = 0
    for i in range(n):
        res += game.run() - 1
        game.reset()


##################### Let's play ####################

def run_random_game(board, n):

    ####### Init Game, Players and Board instances
    #init boardgame
    board = board

    #init players
    RED, BLUE = 1, 2

    player1 = AI(RED, 'random')
    player2 = AI(BLUE, 'random')

    #init game
    game = Game(board, player1, player2)
    #############################################

    res = {i:-1 for i in board_action}

    for action in board.action:
        stock = 0
        # on joue l'action
        # ...

        for _ in range(n):
            # on fini la partie et le winner est 1 ou 2
            stock += winner - 1
        res[action] = stock / n

    ruturn res

#####################################################
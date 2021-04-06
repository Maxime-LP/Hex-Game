#!/usr/bin/env python3
from AI.mc0.Game_aux import Game_aux
from AI.mc0.AI_player import AI_player
from AI.mc0.Board_aux import Board
from copy import deepcopy

##################### Let's play ####################

def best_action(initial_board, n, color):

    # Final dict
    res = {action:0 for action in initial_board.actions}

    (RED, BLUE) = (1, 2) if color == 1 else (2,1)
    player1 = AI_player(RED)
    player2 = AI_player(BLUE)
    possible_plays = initial_board.actions

    #deepcopy doesn't work through pygame objects so elt's do it manually
    tboard = Board(initial_board.size)
    tboard.board = deepcopy(initial_board.board)
    tboard.actions = deepcopy(possible_plays)
    tboard.components = deepcopy(initial_board.components)

    #tboard = deepcopy(initial_board)

    for action in possible_plays:
        games_won = 0

        for _ in range(n):
            tmp_board = deepcopy(tboard)
            tmp_game = Game_aux(tmp_board, player1, player2)
            i, j = action
            tmp_game.players[0].plays(tmp_game.board, i, j)
            winner = tmp_game.run()
            del tmp_game
            del tmp_board
            games_won += (winner == color)

        res[action] = games_won

    best_action = max(res, key = res.get)


    for action, score in res.items():
        if action != best_action:
            print(action,':',round(score/n,3))
        else:
            print("   ",action,':',round(score/n,3))

    return best_action

#####################################################
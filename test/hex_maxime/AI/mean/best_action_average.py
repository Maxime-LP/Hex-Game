#!/usr/bin/env python3
from AI.mean.Game import Game
from AI.mean.AI_player import AI_player
from copy import deepcopy, copy


##################### Let's play ####################

def best_action_average(board, n, color):

    # Final dict
    res = {action:0 for action in board.actions}

    (RED, BLUE) = (1, 2) if color == 1 else (2,1)
    player1 = AI_player(RED)
    player2 = AI_player(BLUE)

    for action in board.actions:
        tboard = deepcopy(board)
        game = Game(tboard, player1, player2)
        i, j = game.board.action_to_coord(action)
        game.players[0].plays(game.board, i, j)

        games_won = 0

        for _ in range(n):
            tgame = deepcopy(game)
            winner = tgame.run()
            games_won += 1 if winner == color else 0

        res[action] = games_won

    print(res)

    best_action = max(res, key = res.get)
    print(best_action)
    return best_action

#####################################################
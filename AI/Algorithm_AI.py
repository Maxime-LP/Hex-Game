import random
from math import sqrt
#from AI.mc.best_action import best_action
from AI.Hex import Hex
from AI.mc.mc import mc
#from AI.mcts.Game_mcts import Hex
from AI.mcts.mcts import mcts

from copy import deepcopy

def run_random(board, color):
    """
    Pick a random legal action.
    """
    return random.choice(board.actions)


def run_mc(board, color):
    """
    Plays n games with random policy for each legal actions.
    Return the action with the best win rate.
    """
    initialState = Hex(color, deepcopy(board))
    searcher = mc(timeLimit=None, iterationLimit=1000)
    action = searcher.search(initialState=initialState, needDetails=True)
    return action

def run_mcts(board, color):
    """
    Uses mcts method with time (ms) or iteration limit.
    """
    initialState = Hex(color, deepcopy(board))
    searcher = mcts(timeLimit=None, iterationLimit= 100, explorationConstant=sqrt(2))
    action = searcher.search(initialState=initialState, needDetails=False)
    return action
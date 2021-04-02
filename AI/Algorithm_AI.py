import random
from math import sqrt
from AI.Hex import Hex
from AI.mc import mc
from AI.mc_ucb1 import mc_ucb1
from AI.mcts import mcts
from copy import deepcopy

def run_random(board, color):
    """
    Pick a random legal action.
    """
    return random.choice(board.actions)


def run_mc(board, color):
    """
    Plays games with iteration or time limit.
    The same number of games is played for each action.
    Random policy is use.
    Return the action with the best win rate.
    """
    initialState = Hex(color, deepcopy(board))
    searcher = mc(timeLimit=None, iterationLimit=board.size**2 * 10)
    action = searcher.search(initialState=initialState, needDetails=False)
    return action

def run_mc_ucb1(board, color):
    """
    Plays games with iteration or time limit.
    The actions are selected with UCB1 criterion.
    Random policy is use.
    Return the action with the best win rate.
    """
    initialState = Hex(color, deepcopy(board))
    searcher = mc_ucb1(timeLimit=None, iterationLimit=49, explorationConstant=sqrt(2))
    action = searcher.search(initialState=initialState, needDetails=False)
    return action

def run_mcts(board, color):
    """
    Uses mcts method with time (ms) or iteration limit.
    """
    initialState = Hex(color, deepcopy(board))
    searcher = mcts(timeLimit=None, iterationLimit=100, explorationConstant=sqrt(2))
    action = searcher.search(initialState=initialState, needDetails=False)
    return action
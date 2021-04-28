from random import choice
from copy import deepcopy
from time import time
from math import sqrt

from AI.Hex import Hex
from AI.mc import MC
from AI.mc_ucb1 import MC_UCB1
from AI.uct import UCT

n = 100

def random(board, color, explorationConstant=None):
    """
    Pick a random legal action.
    """
    return choice(board.actions)


def mc(board, color, explorationConstant=None):
    """
    Plays games with iteration or time limit.
    The same number of games is played for each action.
    Random policy is use.
    Return the action with the best win rate.
    """
    initialState = Hex(color, deepcopy(board))
    searcher = MC(timeLimit=None, iterationLimit=n)
    action = searcher.search(initialState=initialState, needDetails=False)
    return action


def mc_ucb1(board, color, explorationConstant=None):
    """
    Plays games with iteration or time limit.
    The actions are selected with UCB1 criterion.
    Random policy is use.
    Return the action with the best win rate.
    """
    initialState = Hex(color, board)
    searcher = MC_UCB1(timeLimit=None, iterationLimit=n, explorationConstant=explorationConstant)
    action = searcher.search(initialState=initialState, needDetails=False)
    return action


def uct(board, color, tree, explorationConstant=sqrt(2)):
    """
    Plays games with iteration or time limit.
    Uses UCT method and UCB1 criterion for node selection.
    Random policy is use.
    Return the action with the best win rate.
    """
    initialState = Hex(color, deepcopy(board))
    searcher = UCT(timeLimit=None, iterationLimit=n, explorationConstant=explorationConstant)
    tree, action = searcher.search(initialState=initialState, needDetails=False)
    return action


def uct_wm(board, color, tree, explorationConstant=sqrt(2)):
    """
    Plays games with iteration or time limit.
    Uses UCT method and UCB1 criterion for node selection.
    Reuse information from the previously created tree.
    Random policy is use.
    Return the action with the best win rate.
    """
    initialState = Hex(color, deepcopy(board))
    searcher = UCT(timeLimit=None, iterationLimit=n, explorationConstant=explorationConstant)
    new_tree = cut(tree, initialState)
    tree, action = searcher.search(initialState=initialState, needDetails=False, root=new_tree)
    return tree, action


def cut(root, initialState):
    try:
        for child in root.children.values():
            if child.state.board == initialState.board:
                child.parent = None
                return deepcopy(child)
    except AttributeError:
        return None

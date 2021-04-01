import time
from math import log, sqrt
import random
import numpy as np

def randomPolicy(node):
    state = node.state

    while not state.isTerminal():
        try:
            action = random.choice(state.actions)
        except IndexError:
            raise Exception("Non-terminal state has no possible actions: \n" + str(state))
        state = state.takeAction(action, state.currplayer)
    state.winner = state.currplayer
    return state.getReward()


class Node():

    def __init__(self, state, parent):
        self.state = state
        self.isTerminal = state.isTerminal()
        self.isFullyExpanded = self.isTerminal
        self.parent = parent
        self.numVisits = 0
        self.totalReward = 0
        self.children = {}

    def __str__(self):
        s = []
        s.append("totalReward: %s"%(self.totalReward))
        s.append("numVisits: %d"%(self.numVisits))
        s.append("isTerminal: %s"%(self.isTerminal))
        s.append("possibleActions: %s"%(self.children.keys()))
        return "%s: {%s}"%(self.__class__.__name__, ', '.join(s))

class mc():

    def __init__(self, timeLimit=None, iterationLimit=None, explorationConstant=None,
                 rolloutPolicy=randomPolicy):
        if timeLimit != None:
            if iterationLimit != None:
                raise ValueError("Cannot have both a time limit and an iteration limit")
            # time taken for each MCTS search in milliseconds
            self.timeLimit = timeLimit
            self.limitType = 'time'
        else:
            if iterationLimit == None:
                raise ValueError("Must have either a time limit or an iteration limit")
            # number of iterations of the search
            if iterationLimit < 1:
                raise ValueError("Iteration limit must be greater than one")
            self.searchLimit = iterationLimit
            self.limitType = 'iterations'
        self.explorationConstant = explorationConstant
        self.rollout = rolloutPolicy


    def search(self, initialState, needDetails=False):

        self.root = Node(initialState, None)
        actions = self.root.state.actions
        # Note :
        # imputer le temps passé ou les itérations faites
        # plus bas pour comparaison avec mcts
        for action in actions:
            treeNode = Node(self.root.state, self.root)
            self.root.children[action] = treeNode
            self.executeRound(treeNode)

        if self.limitType == 'time':
            timeLimit = time.time() + self.timeLimit / (1000 * len(actions))
            for child in self.root.children.values():
                while time.time() < timeLimit:
                    self.executeRound(child)
        else:
            nb_iter = int(self.searchLimit / len(actions))
            for child in self.root.children.values():
                for i in range(nb_iter):
                    self.executeRound(child)

        bestChild = self.getBestChild(self.root)
        action = (action for action, node in self.root.children.items() if node is bestChild).__next__()

        if needDetails:
            for node, info in self.root.children.items():
                print(node,':',info.totalReward, info.numVisits, info.totalReward/info.numVisits)
            print(action)
            
        return action

    def executeRound(self, node):
        reward = self.rollout(node)
        self.backpropogate(node, reward)


    def backpropogate(self, node, reward):
        while node is not None:
            node.numVisits += 1
            node.totalReward += reward
            node = node.parent


    def getBestChild(self, node):
        bestValue = float("-inf")
        bestNodes = []
        for child in node.children.values():
            nodeValue = child.totalReward / child.numVisits
            if nodeValue > bestValue:
                bestValue = nodeValue
                bestNodes = [child]
            elif nodeValue == bestValue:
                bestNodes.append(child)
        return random.choice(bestNodes)





'''
import time
import math
import random


def randomPolicy(state):
    while not state.isTerminal():
        try:
            action = random.choice(state.getPossibleActions())
        except IndexError:
            raise Exception("Non-terminal state has no possible actions: " + str(state))
        state = state.takeAction(action)
    state.winner = state.currplayer
    return state.getReward()


class mc():

    def __init__(self, timeLimit=None, iterationLimit=None, explorationConstant=math.sqrt(2),
                 rolloutPolicy=randomPolicy):
        if timeLimit != None:
            if iterationLimit != None:
                raise ValueError("Cannot have both a time limit and an iteration limit")
            # time taken for each MCTS search in milliseconds
            self.timeLimit = timeLimit
            self.limitType = 'time'
        else:
            if iterationLimit == None:
                raise ValueError("Must have either a time limit or an iteration limit")
            # number of iterations of the search
            if iterationLimit < 1:
                raise ValueError("Iteration limit must be greater than one")
            self.searchLimit = iterationLimit
            self.limitType = 'iterations'
        self.rollout = rolloutPolicy


    def search(self, initialState, needDetails=False):
        possibleAction = len(initialState.actions)
        if self.limitType == 'time':
            timeLimit = time.time() + self.timeLimit / (1000 * possibleAction)
            for action in initialState.actions:

                while time.time() < timeLimit:
                    self.executeRound()
        else:
            for i in range(self.searchLimit / possibleAction):
                self.executeRound()

        bestChild = self.getBestChild(self.root, 0)
        action = max(res, key = res.get)
        return action


    def evaluateAction(self):
        node = self.selectNode(self.root)
        reward = self.rollout(node.state)
        self.backpropogate(node, reward)

    def selectNode(self, node):
        while not node.isTerminal:
            if node.isFullyExpanded:
                node = self.getBestChild(node, self.explorationConstant)
            else:
                return self.expand(node)
        return node

    def expand(self, node):
        actions = node.state.getPossibleActions()
        for action in actions:
            if action not in node.children:
                newNode = treeNode(node.state.takeAction(action), node)
                node.children[action] = newNode
                if len(actions) == len(node.children):
                    node.isFullyExpanded = True
                return newNode

        raise Exception("Should never reach here")

    def backpropogate(self, node, reward):
        while node is not None:
            node.numVisits += 1
            node.totalReward += reward
            node = node.parent

    def getBestChild(self, node, explorationValue):
        bestValue = float("-inf")
        bestNodes = []
        for child in node.children.values():
            nodeValue = node.state.getCurrentPlayer() * child.totalReward / child.numVisits + explorationValue * math.sqrt(
                2 * math.log(node.numVisits) / child.numVisits)
            if nodeValue > bestValue:
                bestValue = nodeValue
                bestNodes = [child]
            elif nodeValue == bestValue:
                bestNodes.append(child)
        return random.choice(bestNodes)
'''

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
    state.winner = 3 - state.currplayer
    if state.winner==2 & state.getReward()!=0:
        print(state)
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

class mc_ucb1():

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
            self.iterationLimit = iterationLimit
            self.limitType = 'iterations'
        self.explorationConstant = explorationConstant
        self.rollout = rolloutPolicy


    def search(self, initialState, needDetails=False):

        self.root = Node(initialState, None)
        actions = self.root.state.actions
        # Init each node
        for action in actions:
            treeNode = Node(self.root.state, self.root)
            self.root.children[action] = treeNode
            self.executeRound(treeNode)

        if self.limitType == 'time':
            timeLimit = time.time() + self.timeLimit / 1000
            while time.time() < timeLimit:
                child = self.selectNode()
                self.executeRound(child)
        else:
            for i in range(self.iterationLimit):
                child = self.selectNode()
                self.executeRound(child)

        bestChild = self.getBestChild(self.root, self.explorationConstant)
        action = (action for action, node in self.root.children.items() if node is bestChild).__next__()

        if needDetails:
            for node, info in self.root.children.items():
                print(node,':',info.totalReward, info.numVisits, round(info.totalReward/info.numVisits,2))
            print(action)
            
        return action

    def selectNode(self):
        return self.getBestChild(self.root, self.explorationConstant)

    def executeRound(self, node):
        reward = self.rollout(node)
        self.backpropogate(node, reward)


    def backpropogate(self, node, reward):
        while node is not None:
            node.numVisits += 1
            node.totalReward += reward
            node = node.parent


    def getBestChild(self, node, explorationValue):
        bestValue = float("-inf")
        bestNodes = []
        for child in node.children.values():
            nodeValue = child.totalReward / child.numVisits + explorationValue * sqrt(
                log(node.numVisits) / child.numVisits )
            if nodeValue > bestValue:
                bestValue = nodeValue
                bestNodes = [child]
            elif nodeValue == bestValue:
                bestNodes.append(child)
        return random.choice(bestNodes)

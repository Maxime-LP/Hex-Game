import time
from math import log, sqrt
import random
import numpy as np
import networkx as nx
import plotly.graph_objects as go

def randomPolicy(state):

    while not state.isTerminal():
        try:
            action = random.choice(state.actions)
        except IndexError:
            raise Exception("Non-terminal state has no possible actions: \n" + str(state))
        state = state.takeAction(action, state.currplayer)

    return state.getReward()


class treeNode():

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.numVisits = 0
        self.totalReward = 0
        self.children = {}

        #if there is no parent node, state.player (1 or 2) is the player running the mcts algorithm and we want to have the other player as the root node player
        if parent is None : 
            self.player =  3 - state.player
        else:
            self.player = 3 - self.parent.player
    
    def isTerminal(self):
        return self.state.isTerminal()

    def isFullyExpanded(self):
        return len(self.state.actions)==len(self.children)

    def __str__(self):
        s = []
        s.append("totalReward: %s"%(self.totalReward))
        s.append("numVisits: %d"%(self.numVisits))
        s.append("isTerminal: %s"%(self.isTerminal()))
        s.append("possibleActions: %s"%(list(self.children.keys())))
        s.append("player: %s"%(self.player))
        return "%s: {%s}"%(self.__class__.__name__, ', '.join(s))


class mcts():

    def __init__(self, timeLimit=None, iterationLimit=None, explorationConstant=sqrt(2),
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
        self.root = None

    def search(self, initialState, needDetails=False):
        self.root = treeNode(initialState, None)
        if self.limitType == 'time':
            timeLimit = time.time() + self.timeLimit / 1000
            while time.time() < timeLimit:
                self.executeRound()
        else:
            for i in range(self.searchLimit):
                self.executeRound()
        
        bestChild = self.getBestChild(self.root, 0)
        action=(action for action, node in self.root.children.items() if node is bestChild).__next__()
        
        #self.show_graph()

        if needDetails:
            for node, info in self.root.children.items():
                print(node,':',info.totalReward, info.numVisits, round(info.totalReward/info.numVisits,2))
            return action
        else:
            return action

    def executeRound(self):
        """
            execute a selection-expansion-simulation-backpropagation round
        """
        node = self.selectNode(self.root)
        reward = self.rollout(node.state)
        self.backpropogate(node, reward)

    def selectNode(self, node):
        while not node.isTerminal():
            if node.isFullyExpanded():
                node = self.getBestChild(node, self.explorationConstant)
            else:
                return self.expand(node)
        return node

    def expand(self, node):
        actions = node.state.getPossibleActions()
        while actions!=[]:
            action = random.choice(actions)
            if action not in node.children.keys():
                newNode = treeNode(node.state.takeAction(action, node.state.currplayer), node)
                node.children[action] = newNode
                return newNode
        raise Exception("No actions available after this node")

    def backpropogate(self, node, reward):
        """
        reward is the reward of the player who is running the mcts algorithm
        """
        while node is not None:
            node.numVisits += 1
            node.totalReward += (reward == 1) * (node.player != self.root.player)
            node = node.parent

    def getBestChild(self, node, explorationValue):
        bestValue = float("-inf")
        bestNodes = []
        for child in node.children.values():
            nodeValue = child.totalReward / child.numVisits + explorationValue * sqrt(
                log(node.numVisits) / child.numVisits)
            if nodeValue > bestValue:
                bestValue = nodeValue
                bestNodes = [child]
            elif nodeValue == bestValue:
                bestNodes.append(child)
        return random.choice(bestNodes)

'''
    def show_graph(self):
        if self.root is None:
            raise Exception("Can't draw an empty graph")

        G = nx.Graph()
        x,y = 0,0
        G.add_node(self.root,pos=(x,y),score=f"{self.root.totalReward} / {self.root.numVisits}",player=self.root.player,action=Action(player=self.root.player, x='ro', y='ot'))
        
        nodes = self.root.children
        while nodes != {}:
            tmp = {}
            n_to_draw = 0
            y -= 1

            for node in nodes.values():
                children = node.children
                print(children)
                tmp = {**tmp,**children}
                n_to_draw += len(children.values())

            x = -n_to_draw
            for action,node in nodes.items():
                G.add_node(node,pos=(x,y),score=f"{node.totalReward} / {node.numVisits}",player=node.player, action=action)
                G.add_edge(node.parent,node) 
                
                x += 100
                if x==0 and n_to_draw == 0:
                    x += 100

            nodes = tmp
        """
        pos = nx.spring_layout(G)
        for n, p in pos.items():
            G.nodes[n]['pos'] = p
        """
        edge_trace = go.Scatter(
            x = [],
            y = [],
            line = dict(width=0.5, color='#888'),
            hoverinfo = 'none',
            mode = 'lines')

        for edge in G.edges():
            x0, y0 = G.nodes[edge[0]]['pos']
            x1, y1 = G.nodes[edge[1]]['pos']
            
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])
        
        node_trace = go.Scatter(
            x = [],
            y = [],
            text = [],
            mode = 'markers',
            hoverinfo = 'text', # type 
            marker = dict(
                showscale = True,
                colorscale = 'Blues', # couleur du dégradé
                color = 0,
                size = 10, # taille des points
                colorbar = dict(
                    thickness = 15, # largeur barre colorée 
                    title = ' ', # titre barre
                    xanchor='left', # position de la barre
                    titleside='right' # position titre de la barre
                ),
                line=dict(width=2))) # largeur contour des points
        
        for node in G.nodes():
            x, y = G.nodes[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

            node_trace['marker']['color'] += 100 * node.totalReward / (node.numVisits+1)
            node_info = f"{G.nodes[node]['score']}, player : {G.nodes[node]['player']}, action : ({G.nodes[node]['action'].x},{G.nodes[node]['action'].y})"
            node_trace['text'] += tuple([node_info])

        fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title = f"Graph depuis l'etat courant", # titre du graphe
                titlefont = dict(size=16), # taille titre
                showlegend = False,
                hovermode = 'closest',
                margin = dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))
        
        fig.show()
'''

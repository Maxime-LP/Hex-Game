from AI.mean.coord_aux import *
import networkx as nx
from random import choice

"""
Description du fichier.
"""

class AI_player:

    def __init__(self, color):
        self.color = color

    def plays(self, board, i=None, j=None):
        i, j = board.action_to_coord(choice(board.actions))
        board.board[i][j] = self.color

        action = board.coord_to_action(i,j)
        action_index = board.actions.index(action)
        board.played_tiles.append(board.actions.pop(action_index))
        board.graph.add_node((i,j),player=self.color)

        #Creating the edge between the played tile and the neighbood tiles of the same color
        neighbors = board.get_neighbors(i,j)
        color=nx.get_node_attributes(board.graph,'player')

        for neighbor in neighbors:
            if color[neighbor]==self.color:
                board.graph.add_edge(neighbor,(i,j))

        return True
import pygame
import networkx as nx
from AI.Algorithm_AI import run_random, run_ucb1, run_mcts

"""
Description du fichier.
"""

class Player:

    def __init__(self, color):
        self.color = color
        self.name = 'Red player' if self.color==1 else 'Blue player'


    def put_a_stone(self, pos, board, center=False):
        # get the center and the vertices' hex where the current player clicked
        hex_vertices, tile_center = board.get_polygon(pos)
        i, j = board.center_to_coord(tile_center)
        
        if board.board[i][j] == 0:
            board.board[i][j] = self.color
            action = board.coord_to_action(i,j)
            action_index = board.actions.index(action)
            board.played_tiles.append(board.actions.pop(action_index))
            board.graph.add_node((i,j),player=self.color)

            #Creating the edge between the played tile and the neighbourhood tiles of the same color
            neighbours = board.get_neighbors(i,j)
            color=nx.get_node_attributes(board.graph,'player')
            
            for neighbour in neighbours:
                if color[neighbour]==self.color:
                    board.graph.add_edge(neighbour,(i,j))
            return hex_vertices

        else:
            return None
    

class AI(Player):

    def __init__(self, color, algorithm):
        super().__init__(color)

        algorithms = {
                    'random':run_random, 
                    'ucb':run_ucb1, 
                    'mcts':run_mcts
                    }

        self.algorithm = algorithms[algorithm]


    def plays(self, board):
        pos = self.algorithm(board)
        tile_center = board.tiles_centers[board.coord_to_action(pos[0], pos[1])]
        hex_vertices = self.put_a_stone(tile_center, board, True)
        if hex_vertices != None:
            color = 'red' if self.color==1 else 'blue'
            pygame.draw.polygon(board.screen, color, hex_vertices)
            return True


class Human(Player):

    def __init__(self, color):
        super().__init__(color)
   

    def plays(self, board):
        have_play = False
        pos = pygame.mouse.get_pos()
        if board.background.get_at(pos) == (223, 223, 223, 255):
            hex_vertices = self.put_a_stone(pos, board)
            if hex_vertices != None:
                color = 'red' if self.color==1 else 'blue'
                pygame.draw.polygon(board.screen, color, hex_vertices)
                return True

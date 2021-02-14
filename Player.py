import pygame
from Algorithm_AI import run_random, run_ucb1, run_mcts

"""
Description du fichier.
"""

class Player:

    def __init__(self, color):
        self.color = color
        self.name = 'Red player' if self.color==1 else 'Blue player'


    def put_a_stone(self, pos, board, center=False):

        #

        #
        hex_vertices, tile_center = board.get_polygon(pos, center)
        if tile_center not in board.played_tiles:
            i, j = board.list_to_bord(tile_center)
            board.board[i][j] = self.color
            board.played_tiles.append(tile_center)
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
        tile_center = board.tiles_centers[board.board_to_list(pos)]
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

#from misc import get_polygon
import pygame
from Algorithm_AI import run_random, run_ucb1, run_mcts

class Player:

    def __init__(self, color):
        self.color = color
        self.color_trad = {1:'red', 2:'blue'}


    def put_a_stone(self, pos, board):

        hex_vertices, tile_center = board.get_polygon(pos)

        if tile_center not in board.played_tiles:
            i, j = board.list_to_bord(tile_center)
            board.board[i,j] = self.color
            board.played_tiles.append(tile_center)
            return hex_vertices

        else:
            return None

class Human(Player):

    def __init__(self, color):
        super().__init__(color)

    
    def plays(self, board):
        have_play = False
        
        pos = pygame.mouse.get_pos()
        if board.background.get_at(pos) == (223, 223, 223, 255):
            hex_vertices = self.put_a_stone(pos, board)
            if hex_vertices != None:
                pygame.draw.polygon(board.screen, self.color_trad[self.color], hex_vertices)
                return True
    

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
        hex_vertices = self.put_a_stone(pos, board)
        pygame.draw.polygon(board.screen, self.color_trad[self.color], hex_vertices)
        return True
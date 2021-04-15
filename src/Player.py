from misc import display
if display:
    import pygame
    from misc import background, screen
from AI.Algorithm_AI import *


class Player:

    def __init__(self, color):
        self.color = color
        self.name = 'Red player' if self.color==1 else 'Blue player'

    
class Human(Player):

    def __init__(self, color):
        super().__init__(color)
   
    def plays(self, board):
        pos = pygame.mouse.get_pos()
        if background.get_at(pos) == (223, 223, 223, 255):
            return board.update(pos, self.color)

                
class AI(Player):

    def __init__(self, color, algorithm, explorationConstant=sqrt(2)):
        super().__init__(color)
        algorithms = {
                    'random':random,    # random
                    'mc':mc,            # Monte_Carlo
                    'mc_ucb1':mc_ucb1,  # Monte-Carlo + UUpperConfidenceBound 1
                    'uct':uct           # Upper Confidence bounds for Trees
                    }
        self.algorithm_name = algorithm
        self.algorithm = algorithms[algorithm]
        self.explorationConstant = explorationConstant

    def plays(self, board):
        (i,j) = self.algorithm(board, self.color, self.explorationConstant)
        tile_center = board.tiles_centers[board.coord_to_index(i, j)]
        return board.update(tile_center, self.color, True)
    
    def __str__(self):
        return f"{self.color},{self.name},{self.algorithm_name}"
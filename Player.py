import pygame
from AI.Algorithm_AI import run_random, run_mean, run_ucb1, run_mcts


class Player:

    def __init__(self, color):
        self.color = color
        self.name = 'Red player' if self.color==1 else 'Blue player'


    def put_a_stone(self, pos, board, center=False):
        # gets the center and the vertices' hex where the current player is willing to play
        hex_vertices, tile_center = board.get_polygon(pos,center)
        i, j = board.center_to_coord(tile_center)
        
        if board.board[i][j] == 0:
            board.board[i][j] = self.color
            action = board.coord_to_action(i,j)
            action_index = board.actions.index(action)
            board.actions.pop(action_index)

            
            neighbors = board.get_neighbors(i,j)

            # adds tiles to other connected tiles
            added = False
            index = 0
            for component in board.components[self.color-1]:
                if component.intersection(neighbors) != set():
                    board.components[self.color-1][index].add((i,j))
                    added = True
                index += 1

            if not added:
                board.components[self.color-1].append(set([(i,j)]))

            #groups the adjacent components
            l = len(board.components[self.color-1])
            if l > 1:
                for index1 in range(l):
                    for index2 in range(l):
                        if index1 != index2:
                            try:
                                if (i,j) in board.components[self.color-1][index1] and (i,j) in board.components[self.color-1][index2]:
                                    board.components[self.color-1][index1] = board.components[self.color-1][index2] | board.components[self.color-1][index1]
                                    board.components[self.color-1].remove(board.components[self.color-1][index2])                              
                            #in case we are considering an already deleted set
                            except IndexError:
                                pass

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
                color = 'red' if self.color==1 else 'blue'
                pygame.draw.polygon(board.screen, color, hex_vertices)
                return True

                
class AI(Player):

    def __init__(self, color, algorithm):
        super().__init__(color)

        algorithms = {
                    'random':run_random,
                    'mean':run_mean,
                    'ucb':run_ucb1, 
                    'mcts':run_mcts
                    }

        self.algorithm = algorithms[algorithm]


    def plays(self, board):
        pos = self.algorithm(board, self.color)
        tile_center = board.tiles_centers[board.coord_to_action(pos[0], pos[1])]
        hex_vertices = self.put_a_stone(tile_center, board, True)
        if hex_vertices != None:
            color = 'red' if self.color==1 else 'blue'
            pygame.draw.polygon(board.screen, color, hex_vertices)
            return True



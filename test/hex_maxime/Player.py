from coord import *
import networkx as nx
from AI.Algorithm_AI import run_random, run_mean, run_ucb1, run_mcts

"""
Description du fichier.
"""

class Player:

    def __init__(self, color):
        self.color = color
        self.name = 'Red player' if self.color==1 else 'Blue player'
        #self.graph = nx.Graph()


    def put_a_stone(self, board, i, j):

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


class AI(Player):

    def __init__(self, color, algorithm):
        super().__init__(color)

        algorithms = {
                    'random':run_random,
                    'mean': run_mean,
                    'ucb':run_ucb1, 
                    'mcts':run_mcts
                    }

        self.algorithm = algorithms[algorithm]


    def plays(self, board, color):
        i, j = self.algorithm(board, self.color)
        return self.put_a_stone(board, i, j)

class Human(Player):

    def __init__(self, color):
        super().__init__(color)
   

    def plays(self, board, color):

        position = input(f"{self.name} : ")

        #os.system('clear')
        print(f"{self.name} put a stone on {position}.")

        coords = get_coord(position)

        if coords is None:
            print("Coordinates for the stone is incorrect. Please, pick a new one.")
            return False

        line = int(coords[1]) - 1
        column = get_x_index(coords[0]) - 1

        if is_outside(board.board, line, column):
            print(f"{position} is outside the board.")
            return False

        if is_already_taken(board.board, line, column):
            print("A stone already exists at this position.")
            return False

        return self.put_a_stone(board, line, column)

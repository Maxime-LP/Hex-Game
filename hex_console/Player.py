from coord import *
import networkx as nx
from Algorithm_AI import run_random, run_ucb1, run_mcts

"""
Description du fichier.
"""

class Player:

    def __init__(self, color):
        self.color = color
        self.name = 'Red player' if self.color==1 else 'Blue player'
        self.graph = nx.Graph()


    def put_a_stone(self, board, i, j):

        board.board[i][j] = self.color

        action = board.coord_to_action(i,j)
        action_index = board.actions.index(action)
        board.played_tiles.append(board.actions.pop(action_index))
        board.graph.nodes[action]['player'] = self.color

        for neighbor in board.graph.neighbors(action):
            if nx.get_node_attributes(board.graph, 'player')[neighbor]==self.color:
                self.graph.add_edge(action, neighbor)
           
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
        i, j = self.algorithm(board)
        return self.put_a_stone(board, i, j)

class Human(Player):

    def __init__(self, color):
        super().__init__(color)
   

    def plays(self, board):

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

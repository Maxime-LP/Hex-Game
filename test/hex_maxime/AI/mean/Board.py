import string
import networkx as nx
import numpy as np


class Board():

    def __init__(self, board_size):
        self.size = int(board_size)
        #init board with 0 everywhere
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.played_tiles = []

        #Représentation en graph du plateau, ce qui sera utile pour les vérifications de fin de partie
        graph=nx.Graph()
        for i in range(self.size):
            graph.add_nodes_from([(i,j) for j in range(self.size)],player=0)
        self.graph=graph

        self.actions = list(range(self.size**2))
        self.north = 1
        self.south = 2
        self.east = 3
        self.west = 4


    ## Convert point and coord for display ##########################

    def coord_to_action(self, i, j):
        """
        Convert board coord (i,j) to hexagon index in board.actions
        """
        return i * self.size + j


    def action_to_coord(self, action):
        """
        Convert hexagon index in board.actions to board coord (i,j).
        """
        return action // self.size, action % self.size

    ###############################################################


    ## Fonction to create edge between tiles of the same color ########

    def get_neighbors(self, i, j):
        """
        Returns the neighbourhood of a point (i,j) of an hex matrix
        """
        b = np.array(self.board)
        neighbors=[]
        for a in range(-1,2): 
            for b in range(-1,2):  
                if i+a>=0 and j+b>=0 and i+a<self.size and j+b<self.size and (a,b)!=(-1,-1) and (a,b)!=(1,1) and (a,b)!=(0,0):
                    #The neighbour is not outside of the board 
                    neighbors.append((i+a,j+b))
        return neighbors


    ###############################################################


    ## Console display  ###########################################

    def __str__(self):
        """ This function returns a string containing the current state of the board """
        schema = ""
        headers = "     "
        alphabet = list(string.ascii_uppercase) 
        alphabet.reverse()

        red_line_top = headers + "\033[31m--\033[0m" * (len(self.board))

        i = 0
        for line in self.board:
            line_txt = ""
            headers += alphabet.pop() + " "

            line_txt += str(f" {i+1}")  + str(' ' * (i + 1))  + "\033[34m \\ \033[0m" if i < 9 \
                        else str(i + 1) + str(' ' * (i + 1)) + "\033[34m \\ \033[0m"

            for stone in line:
                if stone == 0:
                    line_txt += "⬡ "
                elif stone == 1:
                    line_txt +=  "\033[31m⬢ \033[0m" # 31=red
                else:
                    line_txt += "\033[34m⬢ \033[0m" # 34=blue

            schema += line_txt + "\033[34m \\ \033[0m" + "\n"

            i = i + 1

        red_line_bottom = (" " * (self.size)) + red_line_top

        return headers + "\n" + (red_line_top) + "\n" \
                + schema + red_line_bottom

    ##############################################################

import scipy.linalg as lg
import string
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Board:

    def __init__(self, board_size, background, screen):
        self.size = int(board_size)
        self.board = [[0 for i in range(self.size)] for j in range(self.size)] # np.zeros((self.size, self.size))
        self.played_tiles = []

        #Représentation en graph du plateau, ce qui sera utile pour les vérifications de fin de partie
        graph=nx.Graph()
        for i in range(self.size):
            graph.add_nodes_from([(i,j) for j in range(self.size)])
        self.graph=graph

        self.actions = list(range(self.size**2))
        self.north = 1
        self.south = 2
        self.east = 3
        self.west = 4

        self.background = background
        self.screen = screen

        #center of our homemade landmark
        (x0,y0)=(106,128)
        y0-=20 #initial shift
        x0-=67
        self.tiles_centers = []
        for i in range(1, self.size+1):
            y0 = y0 + 57.7
            x0 +=  33.6
            for j in range(1, self.size+1):
                point = (x0+j*66.7, y0)
                # add hexagon center
                self.tiles_centers.append(point)


## Convert point and coord for display ##############################

    def coord_to_action(self, i, j):
        """
        Convert board coord (i,j) to hexagon index in board.actions
        """
        return i * self.size + j


    def action_to_coord(self, action):
        """Convert hexagon index in board.actions to board coord (i,j)"""
        return action // self.size, action % self.size


    def center_to_coord(self, tile_center):
        """Convert tile_center to board coord (i,j)"""
        index  = self.tiles_centers.index(tile_center)
        i = index // self.size
        j = index % self.size
        return i, j


    def get_polygon(self, pos, center=False):
        """
        Retourne la liste des poss déterminant l'hexagone contenant le pos entré en argument
        L'argument center indique si le pos entré est le pos central de l'hexagone, auquel cas on a pas besoin
        de faire tout un calcul fastidieux
        """

        #Paramètres globaux déterminant la taille des hexagones joués
        l = 64
        h = 74.3

        if center:
            x, y = pos[0], pos[1]
            hex_vertices = [(x+l/2,y-h/4), (x+l/2,y+h/4), (x,y+h/2), (x-l/2,y+h/4), (x-l/2,y-h/4), (x,y-h/2)]
            return hex_vertices, pos

        min_pos = self.tiles_centers[0]
        k = 0

        while True:
            try:
                p = self.tiles_centers[k]
                diff1 = (p[0]-pos[0],p[1]-pos[1])
                diff2 = (min_pos[0]-pos[0],min_pos[1]-pos[1])
                if lg.norm(diff1) < lg.norm(diff2):
                    min_pos = self.tiles_centers[k]
            except IndexError:
                break
            k += 1
        
        x, y = min_pos
        hex_vertices = [(x+l/2,y-h/4),(x+l/2,y+h/4),(x,y+h/2),(x-l/2,y+h/4),(x-l/2,y-h/4),(x,y-h/2)]
        return hex_vertices, min_pos

###############################################################


## Fonction to create edge between tiles of the same color ########

    def get_neighbors(self, i, j):
        """
        It does work with coord we must work with actions in order to 
        create edges.
        """
        b = np.array(self.board)
<<<<<<< Updated upstream
        neighbors = b[(i - 1):(i + 2), (j - 1):(j + 2)].copy()
        #neighbors[0, 0] = 0
        #neighbors[2, 2] = 0
        nb_neighbors = sorted(set(neighbors.flatten().tolist()))
=======
        neighbors=[]
        for x in range(-1,3):
            for y in range(-1,3):
                try:
                    neighbors.append((i+x,j+y))
                except IndexError:
                    #The neighbour is outside of the board !
                    pass
>>>>>>> Stashed changes
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

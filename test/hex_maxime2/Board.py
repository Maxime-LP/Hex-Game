import string
import numpy as np

class Board:

    def __init__(self, board_size):
        self.size = int(board_size)
        self.board = np.zeros((self.size, self.size))
        self.actions = list(range(self.size**2))

        self.east_component = set([(i,self.size) for i in range(self.size)])
        self.west_component = set([(i,-1) for i in range(self.size)])
        self.north_component = set([(-1,i) for i in range(self.size)])
        self.south_component = set([(self.size,i) for i in range(self.size)])

        #Connected components : [ [  compred1, ..., compredq  ],  [   compblue1, ..., compbluer  ]      ]  where comp...i is a list
        #red connected components : self.components[0],  blue connected components : self.components[1]
        self.components = [ [self.north_component, self.south_component], [self.west_component, self.east_component] ]

    ## Convert point and coord for display ##############################

    def coord_to_action(self, i, j):
        """
        Convert board coord (i,j) to hexagon index in board.actions
        """
        return i * self.size + j


    def action_to_coord(self, action):
        """
        Convert hexagon index in board.actions to board coord (i,j)
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
                if (a,b)!=(1,1) and (a,b)!=(0,0) and (a,b)!=(-1,-1):
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

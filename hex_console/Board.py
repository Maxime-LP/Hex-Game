import scipy.linalg as lg
import string
import networkx as nx


class Board(object):

    def __init__(self, board_size):
        self.size = int(board_size)
        #init board with 0 everywhere
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.played_tiles = []
        #(1,1)=0, ..., (size, size)= size^2
        self.actions = list(range(self.size**2))
        self.graph = self.init_graph()


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


    ## Graph with tiles' neighbors ################################

    def init_graph(self):

        size = self.size

        #add node north, east, south, west
        self.north, self.east, self.south, self.west = \
                                [i+self.size**2 for i in range(1,5)]

        #init grid (square)
        square = nx.grid_graph((size, size))
        square = nx.convert_node_labels_to_integers(square)
        #give grid's nodes and edges to G
        G = nx.Graph()
        G.add_nodes_from(square.nodes, player=0)
        G.add_edges_from(square.edges)
        # set player attribute
        nx.set_node_attributes(G, 'player', 0)
        #create edges between tile action and tile action-size
        for j in range(size-1):
            for i in range(1,size):
                x = j + i*size
                y = j + i*size-size + 1 
                G.add_edges_from([(x, y)])

        #add north, east, south and west
        G.add_nodes_from([self.north, self.south], player=1)
        G.add_nodes_from([self.east, self.west], player=2)
        #add edges with tiles
        edges = \
        [(self.north,i) for i in range(size)] + \
        [(self.south,i+size*(size-1)) for i in range(size)] +\
        [(self.east,size*i) for i in range(size)] +\
        [(self.west,size*i+size-1) for i in range(size)]
        G.add_edges_from(edges)

        return G

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

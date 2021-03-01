import networkx as nx
from AI.mean.coord import get_coord
from copy import copy

class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, board, currplayer):
        """
        It checks if there is a path in the graph between two opposite nodes : 
        east and west for the blue player, north and south for the red one.
        If there is a winner, return currplayer for stop the game.
        """
        player=nx.get_node_attributes(self.board.graph,'player')
        size=self.board.size

        if currplayer.color==1:
            #On commence en haut
            for j in range(size):
                upper_node=(0,j)

                if player[upper_node]==1:
                    for i in range(size):
                        lower_node=(size-1,i)
                        
                        if player[lower_node]==1:
                            if nx.has_path(self.board.graph,upper_node,lower_node):
                                return currplayer

        elif currplayer.color==2:
            #On commence à gauche
            for i in range(size):
                left_node=(i,0)

                if player[left_node]==2:
                    for j in range(size):
                        right_node=(j,size-1)

                        if player[right_node]==2:
                            if nx.has_path(self.board.graph,left_node,right_node):
                                return currplayer

        return False


    def run(self):

        while self.on:

            currplayer = self.players[self.turn]

            if currplayer.plays(self.board):
                self.turn = 1 - self.turn
            
            #checks for a win
            winner = self.check_win(self.board, currplayer)

            #if win, declare win and return winner color
            if winner != False:
                self.on = False
                return winner.color
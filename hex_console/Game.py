import networkx as nx
from coord import get_coord
from Board import Board
import os

class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, board, currplayer):
        """
        Check if north and south or east and west are connected. 
        If true return currplayer for stop the game.
        """
        try:
            if nx.has_path(currplayer.graph, board.north, board.south):
                return currplayer
        except nx.exception.NodeNotFound:
            pass
        try:    
            if nx.has_path(currplayer.graph, board.east, board.west):
                return currplayer
        except nx.exception.NodeNotFound:
            pass
            
        return False


    def run(self):

        #print(self.board)

        while self.on:

            currplayer = self.players[self.turn]

            if currplayer.plays(self.board):
                self.turn = 1 - self.turn

            #os.system('clear')
            #print(self.board)
            
            #checks for a win
            winner = self.check_win(self.board, currplayer)

            #if win, declare win and return winner color
            if winner != False:
                self.on = False
                #print(f"It's over! {winner.name} won!")
                return winner.color

    def reset(self):
        self.board = Board(self.board.size)
        self.players[0].graph = nx.Graph()
        self.players[1].graph = nx.Graph()
        self.players = [self.players[0], self.players[1]]
        self.turn = 0
        self.on = True
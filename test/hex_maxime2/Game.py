import numpy as np
from Board import Board

class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True


    def check_win(self, currplayer):
        """
        Checks if a the current player won the game. Returns the winner's name if there is any or None if there is none.

        1 : red player
        2 : blue player
        """

        size=self.board.size
        if currplayer.color==1:
            for component in self.board.components[currplayer.color-1]:

                if self.board.north_component.issubset(component) and self.board.south_component.issubset(component):
                    return currplayer

        elif currplayer.color==2:
            for component in self.board.components[currplayer.color-1]:
                
                if self.board.west_component.issubset(component) and self.board.east_component.issubset(component):
                    return currplayer

        return None


    
    def reset(self):
        """
        Resets the game.
        """
        self.board = Board(self.board.size)
        self.players = [self.players[0], self.players[1]]
        self.turn = 0
        self.on = True


    def run(self):

        while self.on:

            currplayer = self.players[self.turn]

            if currplayer.plays(self.board, currplayer.color):
                self.turn = 1 - self.turn

            # did someone win ?
            winner = self.check_win(currplayer)
            if winner != None:
                self.on = False
                return winner.color

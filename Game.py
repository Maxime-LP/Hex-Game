import numpy as np
import pygame
from time import sleep


class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, currplayer):
        # à supprimer car il y a forcement un gagnant
        if len(self.board.played_tiles) == self.board.size**2:
            return currplayer

        #elif self.currplayer == 1:
        #   return self._is_connected(self._left(), self._right(), 1)
        #return self._is_connected(self._top(), self._bottom(), 2)

        return False
            

    def run(self):

        while self.on:

            for event in pygame.event.get():

                currplayer = self.players[self.turn]

                # when QUIT button is press
                if event.type == pygame.QUIT: 
                    self.on = False
                
                # when ESC button is press
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on = False

                # when curent human player plays
                elif currplayer.__class__.__name__ == 'Human':
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
                        if currplayer.plays(self.board):
                            self.turn = 1 - self.turn
                            print(self.board)
                
                # curent machine player plays
                elif currplayer.__class__.__name__ == 'AI':
                    if currplayer.plays(self.board):
                        self.turn = 1 - self.turn
                        print(self.board)

                #checks for a win
                winner = self.check_win(currplayer)

                #if win, declare win and break loop
                if winner != False:
                    self.on = False
                    print(f"It's over : {winner.name} stones won!")
                    break

                pygame.display.flip()

        return
        
'''
    def reset(self):
        """Resets the game."""
        self.grid = [[EMPTY for _ in range(self.size)]
                     for _ in range(self.size)]
        self._create_graph()
        self.current = BLUE
        self.winner = None
'''
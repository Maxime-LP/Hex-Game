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
        if len(self.board.played_tiles) == self.board.size**2:
            return currplayer
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
                            print(self.board.board)
                
                # curent machine player plays
                elif currplayer.__class__.__name__ == 'AI':
                    sleep(0.2)
                    if currplayer.plays(self.board):
                        self.turn = 1 - self.turn
                        print(self.board.board)

                #checks for a win
                winner = self.check_win(currplayer)

                #if win, declare win and break loop
                if winner != False:
                    self.on = False
                    print(f"It's over : {winner.color_trad[winner.color]} stones won!")
                    break

                pygame.display.flip()

        return
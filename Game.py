import numpy as np
import pygame


class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, player_color):
        # if condition de fin: return players_name
        # si le plateau est plein en attendant ...
        #if len(self.board)==self.N**2:
            #return True
        #if no wins, return false
        return False

    def game_over(self, player_color):
            print(f"It's over! {player_color}s wins!")

    def run(self):

        while self.on:

            currplayer = self.players[self.turn]

            for event in pygame.event.get():

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
                    #pause = input('Press ENTER for run game.')
                    if currplayer.plays(self.board):
                        self.turn = 1 - self.turn
                        print(self.board.board)
                        pause = input('Press ENTER for play AI.')

                #checks for a win
                winner = self.check_win(currplayer)
                #if win, declare win and break loop
                if winner != False:
                    self.game_over(winner.color)
                    self.on = False

            pygame.display.flip()
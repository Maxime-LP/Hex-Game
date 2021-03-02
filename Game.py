import pygame
import numpy as np

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
        """Resets the game."""
        self.board.board = np.zeros((self.board.size, self.board.size))
        self.board.actions = list(range(self.board.size**2))
        self.board.components = [ [self.board.north_component, self.board.south_component], [self.board.west_component, self.board.east_component] ]
        self.turn = 0
        self.on = True
    

    def run(self):

        while self.on:
            for event in pygame.event.get():
                currplayer = self.players[self.turn]

                # upon pressing QUIT button
                if event.type == pygame.QUIT: 
                    self.on = False
                
                # ESC button
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on = False
                
                # when current human player plays
                elif currplayer.__class__.__name__ == 'Human':
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
                        if currplayer.plays(self.board):
                            self.turn = 1 - self.turn
                            print(self.board)
                
                # current computer player plays
                elif currplayer.__class__.__name__ == 'AI':
                    if currplayer.plays(self.board):
                        self.turn = 1 - self.turn
                        print(self.board)

                pygame.display.flip()

                # did someone win ?
                winner = self.check_win(currplayer)
                if winner != None:
                    self.on = False
                    print(f"It's over! {winner.name} won!")
                    break
        return winner.color
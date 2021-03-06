import pygame
import networkx as nx

class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, board, currplayer):
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
                winner = self.check_win(self.board, currplayer)

                #if win, declare win and break loop
                if winner != False:
                    self.on = False
                    print(f"It's over! {winner.name} won!")
                    break

                pygame.display.flip()
        return
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

    def game_over(self, player_name):
            print(f"It's over! {player_name}s wins!")

    def run(self):

        currplayer = self.players[self.turn]

        while self.on:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.on = False
                
                #Lorsque le joueur appuie sur ECHAP
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on = False

                elif currplayer.type == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
                        print(self.board.board)
                        currplayer.put_a_stone_human(self.board)

                elif currplayer.type == 1:
                    #currplayer.plays(self.board)
                    pass

                #checks for a win
                winner = self.check_win(currplayer)
                #if win, declare win and break loop
                if winner != False:
                    self.game_over(winner.color)
                    self.on = False

                #else, switch turns by flipping index in self.players array
                else:
                    self.turn = 1 - self.turn

            pygame.display.flip()


'''
class Player_AI():
    """
    methods : random,ucb1,mcts
    """
    def __init__(self,color,method):
        self.color=color
        self.method=method
    
    def play(self,plateau):
        N1,N2=np.shape(plateau)
        while True:
            if self.method=="random":
                i=npr.randint(0,N1)
                j=npr.randint(0,N2)
                if plateau[i,j]=='.':
                    return i,j

            elif self.method=="ucb1":
                pass

            elif self.method=="mcts":
                pass

'''
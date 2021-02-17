import pygame
import networkx as nx

class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, currplayer):
        #1 correspond au rouge et 2 au bleu
        if currplayer.color==1:
            #On commence en haut
            color=nx.get_node_attributes(self.board.graph,'player')
            for j in range(self.board.size):
                if color[(0,j)]==1:
                    
                    for j in range(self.board.size):
                        if nx.has_path(self.board.graph,(0,j),(self.board.size-1,j)):
                            return currplayer.name
            return None
        else:
            #On commence à gauche
            color=nx.get_node_attributes(self.board.graph,'player')
            #print(self.board.graph.edges())
            for i in range(self.board.size):
                if color[(i,0)]==2:
                    for j in range(self.board.size):
                        if nx.has_path(self.board.graph,(0,j),(self.board.size-1,j)):
                            return currplayer.name
            return None

        """
        if self.board.actions == []:
            return currplayer
        """
        # future condition d'arret
        '''
        elif currplayer.color == 2:
           return self.is_connected(self._left(), self._right(), 1)
        return self.is_connected(self._top(), self._bottom(), 2)
        '''
        return False

    '''    
    def reset(self):
        """Resets the game."""
        self.board.board = np.zeros((self.board.size, self.board.size))
        self.turn = 0
        self.on = True
        self.run()
    '''

    def run(self):

        while self.on:

            for event in pygame.event.get():

                currplayer = self.players[self.turn]

                #checks for a win
                winner = self.check_win(currplayer)

                #if win, declare win and break loop
                if winner != None:
                    self.on = False
                    print(f"It's over! {winner} won!")
                    break

                # when QUIT button is press
                if event.type == pygame.QUIT: 
                    self.on = False
                
                # when ESC button is press
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on = False
                    
                    elif event.key == pygame.K_g:
                        self.board.show_graph()
                
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

                pygame.display.flip()
        return

import pygame
import networkx as nx

class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, currplayer):
        """
        Checks if a the current player won the game. Returns the winner's name if there is any or None if there is none.
        It checks if there is a path in the graph between two opposite nodes : left and right for the blue player, up and down for the red one
        1 : red player
        2 : blue player
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
                                return currplayer.name

        elif currplayer.color==2:
            #On commence à gauche
            for i in range(size):
                left_node=(i,0)

                if player[left_node]==2:
                    for j in range(size):
                        right_node=(j,size-1)

                        if player[right_node]==2:
                            if nx.has_path(self.board.graph,left_node,right_node):
                                return currplayer.name

        return None

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

                # upon pressing QUIT button
                if event.type == pygame.QUIT: 
                    self.on = False
                
                # ESC button
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

                #looking for a winner
                winner = self.check_win(currplayer)
                if winner != None:
                    self.on = False
                    print(f"It's over! {winner} won!")
                    break

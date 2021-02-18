import pygame
import networkx as nx


class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, currplayer):
        '''
        attributes = nx.get_node_attributes(self.board.graph, 'player')
        sub_nodes = [key for key, value in attributes.items() if value == currplayer.color]
        sub_graph = self.board.graph.subgraph(sub_nodes)
        print(sub_graph)
        try:
            if nx.has_path(sub_graph, self.board.north, self.board.south):
                return currplayer
            elif nx.has_path(currplayer.graph, self.board.east, self.board.west):
                return currplayer
        except:
            return False
        '''
        # à optimiser en terme de ligne de codes
        if currplayer.color == 1:
            if (50 in currplayer.graph.nodes) and (52 in currplayer.graph.nodes):
                if nx.has_path(currplayer.graph, self.board.north, self.board.south):
                    return currplayer
        elif (51 in currplayer.graph.nodes) and (53 in currplayer.graph.nodes):
            if nx.has_path(currplayer.graph, self.board.east, self.board.west):
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
                    print(f"It's over! {winner.name} won!")
                    break

                pygame.display.flip()
        return

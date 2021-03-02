from AI.mean.coord_aux import get_coord

class Game:
    
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.turn = 0
        self.on = True

    def check_win(self, board, currplayer):
        size=self.board.size
        if currplayer.color==1:
            for component in self.board.components[currplayer.color-1]:

                if list(set(self.board.north_component) & set(component)) != [] and list(set(self.board.south_component) & set(component)) != [] :
                    return currplayer.name

        elif currplayer.color==2:
            for component in self.board.components[currplayer.color-1]:
                
                if list(set(self.board.west_component) & set(component)) != [] and list(set(self.board.east_component) & set(component)) != [] :
                    return currplayer.name

        return Nonee


    def run(self):

        while self.on:
            currplayer = self.players[self.turn]

            if currplayer.plays(self.board):
                self.turn = 1 - self.turn
            
            winner = self.check_win(self.board, currplayer)

            if winner != False:
                self.on = False
                return winner.color

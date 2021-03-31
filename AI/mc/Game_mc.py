from copy import deepcopy
import string

class Hex():
    
    def __init__(self, color, board):
        self.size = board.size
        self.board = board.board
        self.actions = board.actions
        self.currplayer = color
        self.east_component = board.east_component
        self.west_component = board.west_component
        self.north_component = board.north_component
        self.south_component = board.south_component
        self.components = board.components
        self.winner = None
        self.player = color

    def getCurrentPlayer(self):
        return self.currplayer

    def getPossibleActions(self):
        return self.actions

    def getNeighbors(self, i, j):
        """
        Returns the neighbourhood of a point (i,j) of an hex matrix
        """
        neighbors=[]
        for a in range(-1,2): 
            for b in range(-1,2):  
                if (a,b)!=(1,1) and (a,b)!=(0,0) and (a,b)!=(-1,-1):
                    neighbors.append((i+a,j+b))
        return neighbors

    def takeAction(self, action, currplayer):
        new_state = deepcopy(self)
        (i,j) = action
        new_state.board[i][j] = currplayer
        new_state.actions.remove((i,j))
        neighbors = self.getNeighbors(i, j)
        added = False
        index = 0
        for component in new_state.components[currplayer-1]:
            if component.intersection(neighbors) != set():
                new_state.components[currplayer-1][index].add((i,j))
                added = True
            index += 1

        if not added:
            new_state.components[currplayer-1].append(set([(i,j)]))
        
        #groups the adjacent components
        length = len(new_state.components[currplayer-1])
        if length > 1:
            for index1 in range(length):
                for index2 in range(length):
                    if index1 != index2:
                        try:
                            #in case we are considering an already deleted list
                            if (i,j) in new_state.components[currplayer-1][index1] and (i,j) in new_state.components[currplayer-1][index2]:
                                new_state.components[currplayer-1][index1] = new_state.components[currplayer-1][index2] | new_state.components[currplayer-1][index1]
                                new_state.components[currplayer-1].remove(new_state.components[currplayer-1][index2])
                        except IndexError:
                            pass

        new_state.currplayer = 3 - currplayer
        
        return new_state
    

    def isTerminal(self):
        size = len(self.board)
        currplayer = 3 - self.currplayer
        if currplayer == 1:
            for component in self.components[currplayer-1]:
                if self.north_component.issubset(component) and self.south_component.issubset(component):
                    return True

        elif currplayer == 2:
            for component in self.components[currplayer-1]:
                if self.west_component.issubset(component) and self.east_component.issubset(component):
                    return True
        return False


    def getReward(self):
        if self.winner != None:
            return 1 if self.winner == self.player else 0
        return False


class Action():

    def __init__(self, player, i, j):
        self.player = player
        self.i = i
        self.j = j

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y and self.player == other.player

    def __hash__(self):
        return hash((self.x, self.y, self.player))

from AI.mean.coord_aux import *
from random import choice


class AI_player:

    def __init__(self, color):
        self.color = color


    def put_a_stone(self, board, i, j):

        board.board[i][j] = self.color
        action = board.coord_to_action(i,j)
        action_index = board.actions.index(action)
        board.actions.pop(action_index)

        #adds the center of the polygon to the player connected component
        neighbors = board.get_neighbors(i,j)
        added=False
        index=0
            
        while index < len(board.components[self.color-1]):
            for neighbor in neighbors:
                if neighbor in board.components[self.color-1][index]:
                    board.components[self.color-1][index].append((i,j))
                    added=True
                    break
            index+=1

        if not added:
            #ie if all the neighbors are not in any of the player's connected components ie if the neighbors are not of the player's color
            board.components[self.color-1].append([(i,j)])


        #groups the adjacent components
        length = len(board.components[self.color-1])
        if length>1:
            for index1 in range(length):
                for index2 in range(length):
                    if index1!=index2:
                        try:
                            #in case we are considering an already deleted list
                            if (i,j) in board.components[self.color-1][index1] and (i,j) in board.components[self.color-1][index2]:
                                board.components[self.color-1][index1]+=board.components[self.color-1][index2]
                                board.components[self.color-1][index1].remove((i,j))
                                board.components[self.color-1].remove(board.components[self.color-1][index2])
                        except IndexError:
                            pass

        return True


    def plays(self, board, i=None, j=None):
        if i == None:
            i, j = board.action_to_coord(choice(board.actions))
        return self.put_a_stone(board, i, j)
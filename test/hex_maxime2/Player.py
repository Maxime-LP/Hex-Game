from AI.Algorithm_AI import run_random, run_mean, run_ucb1, run_mcts


class Player:

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
                    board.components[self.color-1][index].add((i,j))
                    added=True
                    break
            index+=1

        if not added:
            #ie if all the neighbors are not in any of the player's connected components ie if the neighbors are not of the player's color
            board.components[self.color-1].append(set([(i,j)]))


        #groups the adjacent components
        length = len(board.components[self.color-1])
        if length>1:
            for index1 in range(length):
                for index2 in range(length):
                    if index1!=index2:
                        try:
                            if (i,j) in board.components[self.color-1][index1] and (i,j) in board.components[self.color-1][index2]:
                                board.components[self.color-1][index1] = board.components[self.color-1][index2] | board.components[self.color-1][index1]
                                board.components[self.color-1].remove(board.components[self.color-1][index2])
                                
                        #in case we are considering an already deleted set
                        except IndexError:
                            pass
        return True

class AI(Player):

    def __init__(self, color, algorithm):
        super().__init__(color)

        algorithms = {
                    'random':run_random,
                    'mean':run_mean,
                    'ucb':run_ucb1, 
                    'mcts':run_mcts
                    }

        self.algorithm = algorithms[algorithm]


    def plays(self, board, color):
        i, j = self.algorithm(board, self.color)
        return self.put_a_stone(board, i, j)
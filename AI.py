from config import N
from misc import tiles_centers
import numpy.random as npr

class Player_AI():
    """
    methods : random,ucb1,mcts
    """
    def __init__(self,color,method):
        self.color=color
        self.method=method
    
    def joue(self,plateau):

        while True:

            if self.method=="random":
                i=npr.randint(0,N)
                j=npr.randint(0,N)

                if plateau[i,j]=='.':
                    return i,j

            elif self.method=="ucb1":
                pass
            elif self.method=="mcts":
                pass


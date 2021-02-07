import numpy.random as npr
from misc import get_polygon

class Player_AI():
    """
    methods : random,ucb1,mcts
    """
    def __init__(self,color,method):
        self.color=color
        self.method=method
    
    def play(self,plateau):

        while True:
            N=self.N
            self.b
            if self.method=="random":
                i=npr.randint(0,self.N)
                j=npr.randint(0,self.N)
                if plateau[i,j]=='.':
                    return i,j

            elif self.method=="ucb1":
                pass

            elif self.method=="mcts":
                pass

class Game():
    l=64
    h=74.3
    def __init__(self,gamemode,N,human_color,method):
        self.gamemode=gamemode
        self.N=N
        #le joueur bleu commence
        self.turn="blue"

        #plateau lisible par nos algorithmes
        plateau=[['.' for i in range(N)] for j in range(N)]
        plateau=np.array(plateau)
        self.plateau=plateau
        self.played_tiles=played_tiles=[]

        if self.gamemode!="hvsh":
            self.human_color=human_color
        if gamemode=="aivsai":
            self.red=Player_AI("red",method)
            self.blue=Player_AI("blue",method)
        elif gamemode=="hvsai":
            human_color=sys.argv[2]
            if human_color=="blue":
                AI_color="red"
            else:
                AI_color="blue"
            self.AI=Player_AI(AI_color,method)
        
        ###Liste des centres des hexagones
        #Centre de notre repère "fait-maison"
        (x0,y0)=(106,128)
        #On se donne la liste des centres des hexagones
        self.tiles_centers=[]
        y0-=20 #initial shift
        x0-=67
        for i in range(1,N+1):
            y0=y0+57.7
            x0+=33.6
            for j in range(1,N+1):
                point=(x0+j*66.7,y0)
                self.tiles_centers.append(point)

    def convert(self,i,j):
        """
        Convertit les coordonnées (i,j) du plateau en l'indice de l'hexagone correspondant
        """
        return i*self.N + j

    def play_turn(self,pos):
        if self.gamemode=="hvsh" or (self.gamemode=="hvsai" and self.turn==self.human_color):

            points,center=get_polygon(pos,l,h)
            if center not in self.played_tiles:
                    index=self.tiles_centers.index(center)
                    i,j=index//N,index%N                                #Si q et r sont tq index = N*q+r alors on a bien i,j = q,r
                    self.played_tiles.append(center)
            else:
                points=None
            
        elif (self.gamemode=="hvsai" and self.turn!=self.human_color) or self.gamemode=="aivsai":

            if self.gamemode=="hvsai":
                i,j=self.AI.play(plateau)
            elif self.gamemode=="aivsai":
                if self.turn=="blue":
                    i,j=self.blue.play(plateau)
                else:
                    i,j=self.AI.play(plateau)

            index=convert(i,j)
            x,y=self.tiles_centers[index]
            points=[(x+l/2,y-h/4),(x+l/2,y+h/4),(x,y+h/2),(x-l/2,y+h/4),(x-l/2,y-h/4),(x,y-h/2)]
            self.played_tiles.append((x,y))
        
        if points!=None:
            self.plateau[i,j]=self.turn
            if self.turn=="red":
                self.turn="blue"
            else: self.turn="red"
            return points
        else:
            return points

    def IsOver(self):
        """
        returns the state of the game (finished or not)
        """
        if len(self.played_tiles)==self.N**2:
            return True



        






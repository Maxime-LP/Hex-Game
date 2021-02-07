import numpy.random as npr
from misc import get_polygon
import numpy as np

###
#Paramètres globaux déterminant la taille des hexagones joués
l=64
h=74.3
###

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

class Game():
    def __init__(self,gamemode,N,human_color=None,method=None,starter="blue"):
        self.gamemode=gamemode
        self.N=int(N)
        self.turn=starter

        #plateau lisible par nos algorithmes
        plateau=[['.' for i in range(self.N)] for j in range(self.N)]
        plateau=np.array(plateau)
        self.plateau=plateau
        self.played_tiles=played_tiles=[]

        if self.gamemode=="hvsh":
            self.human_color=human_color
        elif self.gamemode=="aivsai":
            self.red=Player_AI("red",method)
            self.blue=Player_AI("blue",method)
        elif self.gamemode=="hvsai":
            self.human_color=human_color
            if self.human_color=="blue":
                self.AI_color="red"
            else:
                self.AI_color="blue"
            self.AI=Player_AI(self.AI_color,method)
        
        ###Liste des centres des hexagones
        #Centre de notre repère "fait-maison"
        (x0,y0)=(106,128)
        #On se donne la liste des centres des hexagones
        self.tiles_centers=[]
        y0-=20 #initial shift
        x0-=67
        for i in range(1,self.N+1):
            y0=y0+57.7
            x0+=33.6
            for j in range(1,self.N+1):
                point=(x0+j*66.7,y0)
                self.tiles_centers.append(point)

    def convert(self,i,j):
        """
        Convertit les coordonnées (i,j) du plateau en l'indice de l'hexagone correspondant
        """
        return i*self.N + j

    def play_turn(self,pos=None):
        """
        Retourne les points determinants l'hexagone joué et la couleur de joueur
        Retourne None,color si l'emplacement choisi est occupé
        """
        if self.gamemode=="hvsh" or (self.gamemode=="hvsai" and self.turn==self.human_color):

            points,center=get_polygon(pos,l,h,self.tiles_centers)
            if center not in self.played_tiles:
                    index=self.tiles_centers.index(center)
                    i,j=index//self.N,index%self.N                                #Si q et r sont tq index = N*q+r alors on a bien i,j = q,r
                    self.played_tiles.append(center)
            else:
                points=None
            
        elif (self.gamemode=="hvsai" and self.turn!=self.human_color) or self.gamemode=="aivsai":
            if self.gamemode=="hvsai":
                i,j=self.AI.play(self.plateau)
            elif self.gamemode=="aivsai":
                if self.turn=="blue":
                    i,j=self.blue.play(self.plateau)
                else:
                    i,j=self.red.play(self.plateau)

            index=self.convert(i,j)
            x,y=self.tiles_centers[index]
            points,center=get_polygon((x,y),l,h,center=True)
            self.played_tiles.append(center)
        
        color=self.turn
        if points!=None:
            self.plateau[i,j]=self.turn
            if self.turn=="red":
                self.turn="blue"
            else: self.turn="red"
            return points,color
        else:
            return points,color

    def IsOver(self):
        """
        returns the state of the game (finished or not)
        """
        #version pour tester, il faudrait aussi retourner le vainqueur
        if len(self.played_tiles)==self.N**2:
            return True
        else:
            return False
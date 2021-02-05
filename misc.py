import scipy.linalg as lg
from config import N
"""
Miscellanous functions
"""

#Centre de notre repère "fait-maison"
(x0,y0)=(106,128)

l=64
h=74.3

#On se donne la liste des centres des hexagones
tiles_centers=[]
y0-=20 #initial shift
x0-=67
for i in range(1,N+1):
    y0=y0+57.7
    x0+=33.6
    for j in range(1,N+1):
        point=(x0+j*66.7,y0)
        tiles_centers.append(point)

def get_polygon(point):
    """
    Retourne la liste des points déterminant le polygone contenant le point en argument
    """
    min_point=tiles_centers[0]
    k=0
    while True:
        try:
            p=tiles_centers[k]
            diff1=(p[0]-point[0],p[1]-point[1])
            diff2=(min_point[0]-point[0],min_point[1]-point[1])
            if lg.norm(diff1)<lg.norm(diff2):
                min_point=tiles_centers[k]
        except IndexError:
            break
        k+=1
    
    x,y=min_point
    points=[(x+l/2,y-h/4),(x+l/2,y+h/4),(x,y+h/2),(x-l/2,y+h/4),(x-l/2,y-h/4),(x,y-h/2)]
    return points,min_point

def convert(i,j):
    """
    Convertit les coordonnées (i,j) en l'indice de l'hexagone correspondant
    """

    return i*N + j
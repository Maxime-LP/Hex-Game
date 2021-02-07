import scipy.linalg as lg
"""
Miscellanous functions
"""
def get_polygon(point,l,h):
    """
    Retourne la liste des points déterminant le polygone contenant le point entré en argument
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


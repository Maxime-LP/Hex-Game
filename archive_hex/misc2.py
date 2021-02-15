import scipy.linalg as lg
"""
Miscellanous functions
"""
def get_polygon(point,l,h,tiles_centers=None,center=False):
    """
    Retourne la liste des points déterminant l'hexagone contenant le point entré en argument
    L'argument center indique si le point entré est le point central de l'hexagone, auquel cas on a pas besoin
    de faire tout un calcul fastidieux
    """

    if center:
        x,y=point
        return [(x+l/2,y-h/4),(x+l/2,y+h/4),(x,y+h/2),(x-l/2,y+h/4),(x-l/2,y-h/4),(x,y-h/2)],point

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
class Board:

    def __init__(self, board_size, background, screen):
        self.size = int(board_size)
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.played_tiles = []
        self.background = background
        self.screen = screen

        #Centre de notre repère "fait-maison"
        (x0,y0)=(106,128)
        y0-=20 #initial shift
        x0-=67
        self.tiles_centers = []
        for i in range(1, self.size+1):
            y0 = y0 + 57.7
            x0 +=  33.6
            for j in range(1, self.size+1):
                point = (x0+j*66.7, y0)
                # on ajoute le centre des hexagones
                self.tiles_centers.append(point)

    def convert(self,i,j):
        """
        Convertit les coordonnées (i,j) du plateau en l'indice de l'hexagone correspondant
        """
        return i*self.N + j
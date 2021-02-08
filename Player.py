from misc import get_polygon
import pygame

class Player:

    def __init__(self, player_type, color, played_tiles):
        #self.name = ...
        self.type = int(player_type)
        self.color = color
        self.plays = played_tiles

    def put_a_stone(self, pos, board):
        points, center = get_polygon(pos, board.tiles_centers)
        if center not in board.played_tiles:
            index  = board.tiles_centers.index(center)
            i, j = index//board.size, index%board.size                               #Si q et r sont tq index = N*q+r alors on a bien i,j = q,r
            board.played_tiles.append(center)
        else:
            points = None
        
        if points != None:
            board.board[i][j] = self.color
            return board, points
        else:
            return board, points


    def put_a_stone_human(self, board):
        pos = pygame.mouse.get_pos()
        if board.background.get_at(pos) == (223, 223, 223, 255):
            board, points = self.put_a_stone(pos, board)
            #points=None si le joueur clique sur une case non valide
            if points != None:
                pygame.draw.polygon(board.screen, self.color, points)

    def put_a_stone_ai(self, board):
        points = currplayer.put_a_stone()
        pygame.draw.polygon(screen,color,points)

'''    
class Human(Player):

    def plays(self, board):
        return

class AI(Player):

    def plays(self, board):
        points = currplayer.put_a_stone()
        pygame.draw.polygon(screen,color,points)
'''
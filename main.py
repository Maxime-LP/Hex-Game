#!/usr/bin/env python3

import pygame
import numpy as np
from misc import get_polygon,tiles_centers
from config import N

pygame.init()
screen = pygame.display.set_mode((1300,900))
background = pygame.image.load(f"Hex_board_{N}.png")

#   0__________________x=1300
#   |
#   | (x0,y0)
#   |  
#   |       screen
#   |
#   y=900


#appliquer l'image du plateau de jeu
screen.blit(background,(0,0))

#plateau lisible par nos algorithmes
plateau=[['.' for i in range(N)] for j in range(N)]
plateau=np.array(plateau)


#####Initialisation
#Liste des hexagones posés
played_tiles=[]
#Le joueur bleu commence
color="blue"
pygame.display.set_caption("Homemade Hex Game")
last_played_tile=None
running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            break
        
        #Lorsque le joueur appuie sur ECHAP
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

        #Au clic gauche de la souris
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
            #On récupère la position de la souris sous la forme pos=(x,y)
            pos=pygame.mouse.get_pos()

            if background.get_at(pos)==(223, 223, 223, 255):
                points,center=get_polygon(pos)

                if center not in played_tiles:
                    #On dessine l'hexagone au lieu sélectionné et on change de joueur
                    pygame.draw.polygon(screen,color,points)
                    last_played_tile=center
                    played_tiles.append(center)
                    index=tiles_centers.index(center)
                    i,j=index//N,index%N #on pourra verifier que si q et r sont tq index=11q+r alors on a bien i,j=q,r
                    plateau[i,j]=color
                    print(plateau)
                    if color=="red": color="blue"
                    else: color="red"
    
    pygame.display.flip()

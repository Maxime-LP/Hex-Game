#!/usr/bin/env python3
import sys
import pygame
import numpy as np
from misc import get_polygon,tiles_centers,convert,l,h
from config import N
from AI import Player_AI

#####Initialisations
pygame.init()
screen = pygame.display.set_mode((1300,900))
background = pygame.image.load(f"Hex_board_{N}.png")
pygame.display.set_caption("Homemade Hex Game")


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

played_tiles=[]

#Type de partie
#hvsh (human vs human), hvsai (human vs ai), aivsai (ai vs ai)
gamemode=sys.argv[1]

if gamemode=="aivsai":
    AI1=Player_AI("red","random")
    AI2=Player_AI("blue","random")
elif gamemode=="hvsai":
    human_color=sys.argv[2]
    if human_color=="blue":
        AI_color="red"
    else:
        AI_color="blue"
    AI=Player_AI(AI_color,"random")

#Selection du joueur de départ
color="blue"

it=0

running=True
while running and it<N*N:
    #integrer un critère d'arrêt
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            break
        
        #Lorsque le joueur appuie sur ECHAP
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

        #Au clic gauche de la souris et si la partie implique un joueur humain
        elif gamemode=="hvsh" and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
            #On récupère la position de la souris sous la forme pos=(x,y)
            pos=pygame.mouse.get_pos()

            if background.get_at(pos)==(223, 223, 223, 255):
                points,center=get_polygon(pos)

                if center not in played_tiles:
                    #On dessine l'hexagone au lieu sélectionné et on change de joueur
                    pygame.draw.polygon(screen,color,points)
                    index=tiles_centers.index(center)
                    i,j=index//N,index%N #Si q et r sont tq index=11q+r alors on a bien i,j=q,r
                    played_tiles.append(center)
                    plateau[i,j]=color
                    print(plateau)
                    if color=="red": color="blue"
                    else: color="red"
                    it+=1

        elif gamemode=="hvsai":
            if color==human_color and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
                #On récupère la position de la souris sous la forme pos=(x,y)
                pos=pygame.mouse.get_pos()

                if background.get_at(pos)==(223, 223, 223, 255):
                    points,center=get_polygon(pos)

                    if center not in played_tiles:
                        #On dessine l'hexagone au lieu sélectionné et on change de joueur
                        pygame.draw.polygon(screen,color,points)
                        index=tiles_centers.index(center)
                        i,j=index//N,index%N #Si q et r sont tq index=11q+r alors on a bien i,j=q,r
                        played_tiles.append(center)
                        plateau[i,j]=color
                        print(plateau)
                        if color=="red": color="blue"
                        else: color="red"
                        it+=1

            
            elif color==AI_color:
                i,j=AI.joue(plateau)
                plateau[i,j]=color
                index=convert(i,j)
                x,y=tiles_centers[index]
                points=[(x+l/2,y-h/4),(x+l/2,y+h/4),(x,y+h/2),(x-l/2,y+h/4),(x-l/2,y-h/4),(x,y-h/2)]
                played_tiles.append((x,y))
                pygame.draw.polygon(screen,color,points)

                if color=="red": color="blue"
                else: color="red"
                it+=1

        elif gamemode=="aivsai":

            if color=="red":
                i,j=AI1.joue(plateau)
                plateau[i,j]=color
                index=convert(i,j)
                x,y=tiles_centers[index]
                points=[(x+l/2,y-h/4),(x+l/2,y+h/4),(x,y+h/2),(x-l/2,y+h/4),(x-l/2,y-h/4),(x,y-h/2)]
                played_tiles.append((x,y))
                pygame.draw.polygon(screen,color,points)
                color="blue"
            else:
                i,j=AI2.joue(plateau)
                plateau[i,j]=color
                index=convert(i,j)
                x,y=tiles_centers[index]
                points=[(x+l/2,y-h/4),(x+l/2,y+h/4),(x,y+h/2),(x-l/2,y+h/4),(x-l/2,y-h/4),(x,y-h/2)]
                played_tiles.append((x,y))
                pygame.draw.polygon(screen,color,points)
                color="red"
            
            it+=1

    pygame.display.flip()

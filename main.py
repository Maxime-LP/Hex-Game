#!/usr/bin/env python3
import sys
import pygame
import numpy as np
from classes import Player_AI,Game

#python main.py gamemode taille_plateau human_color ai_method
#Type de partie : hvsh (human vs human), hvsai (human vs ai), aivsai (ai vs ai)
Hex=Game(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
N=Hex.N

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

running=True
while running:

    if Hex.IsOver():
        break

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
                points=Hex.play_turn(pos)
                if points!=None:
                    pygame.draw.polygon(screen,Hex.turn,points)
                    it+=1

        elif gamemode=="hvsai":
            if Hex.turn==Hex.human_color and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
                #On récupère la position de la souris sous la forme pos=(x,y)
                pos=pygame.mouse.get_pos()

                if background.get_at(pos)==(223, 223, 223, 255):
                    points,color=Hex.play_turn(pos)
                    if points!=None:
                        pygame.draw.polygon(screen,color,points)

            elif Hex.turn==Hex.AI_color:
                points,color=Hex.play_turn(pos)
                pygame.draw.polygon(screen,color,points)

        elif gamemode=="aivsai":
            points,color=Hex.play_turn(pos)
            pygame.draw.polygon(screen,color,points)

    pygame.display.flip()
input()

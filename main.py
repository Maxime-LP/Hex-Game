#!/usr/bin/env python3
import sys
import pygame
import numpy as np
from classes import Player_AI,Game

"""
Utilisation :
    
    python main.py gamemode taille_plateau human_color ai_method starter

gamemode : hvsh (human vs human), hvsai (human vs ai), aivsai (ai vs ai)
taille_plateau : 11 pour 11x11 ou 7 pour 7x7
human_color : la couleur du joueur humain (dans le cas d'une partie hvsh ou aivsai, ce paramètre n'a pas d'importance)
ai_method : méthode de jeu du joueur artificiel (random, ucb1 ou mcts)
starter : couleur du joueur de départ

pour le moment il faut tout mettre
"""
Hex=Game(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])

#####Initialisations
pygame.init()
screen = pygame.display.set_mode((1300,900))
background = pygame.image.load(f"Hex_board_{Hex.N}.png")
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

############################Boucle principale
running=True
while running:
    if Hex.IsOver():
        #Pour marquer une pause avant de sortir
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running=False
        
        #Lorsque le joueur appuie sur ECHAP
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False

        #Au clic gauche de la souris et si la partie implique un joueur humain
        elif Hex.gamemode=="hvsh" and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
            #On récupère la position de la souris sous la forme pos=(x,y)
            pos=pygame.mouse.get_pos()
            if background.get_at(pos)==(223, 223, 223, 255):
                points,color=Hex.play_turn(pos)
                if points!=None:
                    #points=None si le joueur clique sur une case non valide
                    pygame.draw.polygon(screen,color,points)

        elif Hex.gamemode=="hvsai":
            if Hex.turn==Hex.human_color and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
                pos=pygame.mouse.get_pos()
                if background.get_at(pos)==(223, 223, 223, 255):
                    points,color=Hex.play_turn(pos)
                    if points!=None:
                        #points=None si le joueur clique sur une case non valide
                        pygame.draw.polygon(screen,color,points)

            elif Hex.turn==Hex.AI_color:
                points,color=Hex.play_turn()
                pygame.draw.polygon(screen,color,points)

        elif Hex.gamemode=="aivsai":
            points,color=Hex.play_turn()
            pygame.draw.polygon(screen,color,points)

    pygame.display.flip()
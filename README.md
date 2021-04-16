# Hex-Game

Hex est un jeu de société pour deux personnes dans lequel les joueurs essaient de relier les côtés opposés d'une grille hexagonale. Hex est intéressant car malgré des règles extrêmement simples le jeu offre une grande compléxité : cinq milliards de fois plus de positions possibles que les échecs (sur un plateau de 11x11). Cette grande profondeur signifie que le jeu reste difficile à jouer pour les ordinateurs.

## Comment jouer ?

Lorsque c'est votre tour, cliquez sur une cellule vide pour la marquer de votre couleur. Essayez de créer un chemin reliant vos deux côtés du plateau.

Il est possible de jouer contre une IA, dont plusieurs implémentations sont disponibles : 
- random
- mc
- mc_ucb1
- mcts

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Hex_board_11x11.svg/800px-Hex_board_11x11.svg.png)

## Setup

### Package requis
pygame

### Lancement d'une patie
Pour lancer une partie, saisir dans le terminal : 

*./main.py joueur_1 joueur_2 taille_du_plateau affichage

joueur_1 et joueur_2 : 'h' pour un joueur humain et 'random', 'mc', 'mc_ucb1' ou 'mcts' pour une IA, correspondant à la méthode implémentée. 
Taille_du_plateau : 7 ou 11
affichage : 0 (pas d'affichage) ou 1

### Tests

Dans le fichier test.py est implémenté deux fonctions:
- une permettant de trouver la meilleur constante pour UCT au jeu de Hex (Spoiler : 0.4).
- un autre pour se faire affronter deux IA.

Les commandes sont de la forme:

```bash
./test.py AI1Name AI2Name 7 0 testName
```

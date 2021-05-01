# Hex-Game

Hex est un jeu de société pour deux personnes dans lequel les joueurs essaient de relier les côtés opposés d'une grille hexagonale. Hex est intéressant car malgré des règles extrêmement simples le jeu offre une grande compléxité : cinq milliards de fois plus de positions possibles que les échecs (sur un plateau de 11x11). Cette grande profondeur signifie que le jeu reste difficile à jouer pour les ordinateurs.

## Comment jouer ?

Lorsque c'est votre tour, cliquez sur une cellule vide pour la marquer de votre couleur. Essayez de créer un chemin reliant vos deux côtés du plateau.

Il est possible de jouer contre une IA, dont plusieurs implémentations sont disponibles : 
- random
- mc
- mc_ucb1
- [uct](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
- uct_wm

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Hex_board_11x11.svg/800px-Hex_board_11x11.svg.png" height="300" />

## Setup

```bash
$ # Get the code
$ git clone https://github.com/Maxime-LP/Hex-Game/main
$ cd Hex-Game
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ pip3 install -r requirements.txt
```

## Start a game

```bash
$ ./main.py player1_type player2_type board_size
```

*player1_type*/*player2_type*: 'h' for human player and 'random', 'mc', 'mc_ucb1', 'uct' or 'uct_wm for AI, correspond to implemented method. 
*board_size*: 7 or 11

## Test

```bash
$ ./test.py AI1_name AI2_name board_size num_games_to_simulate save
```

*board_size*: within the limit of the computing power
*num_games_to_simulate*: number of game to simulate per constant (the list of constants can be modified in the test.py file)
*save*: write "save" if you want to save the results of the simulation, otherwise nothing


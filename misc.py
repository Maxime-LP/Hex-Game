import sys
import pygame
display = bool(int(sys.argv[4]))
if display:
    board_size = sys.argv[3]
    background = pygame.image.load(f"img/Hex_board_{board_size}.png")
    screen = pygame.display.set_mode((1300,900))
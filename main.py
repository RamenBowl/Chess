import Chess
from Board import Board

from Piece import Piece

import pygame, sys
from pygame.locals import *

pygame.init()
SIZE = WIDTH,HEIGHT = 800, 800

ROWS = 8
COLS = 8

SQUARE_HEIGHT = HEIGHT//ROWS
SQUARE_WIDTH = WIDTH//COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Chess")

screen.fill(BLACK)

for row in range(ROWS):
    for col in range(COLS):
        if((row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1)):
            pygame.draw.rect(screen, WHITE, (row * SQUARE_HEIGHT, col * SQUARE_WIDTH, SQUARE_HEIGHT, SQUARE_WIDTH))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
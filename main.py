import Chess
from Game import Game

from Piece import Piece

import pygame, sys
from pygame.locals import *
from const import *

pygame.init()

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Chess")
        self.game = Game()

    def playGame(self):
        game = self.game
        screen = self.screen

        while True:
            game.showBoard(screen)
            game.showPieces(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.playGame()
from tkinter import Pack
import pygame

from Board import Board
from const import *

class Game:
    def __init__(self):
        self.board = Board()

    def showBoard(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                rect = (row * SQUARE_HEIGHT, col * SQUARE_WIDTH, SQUARE_HEIGHT, SQUARE_WIDTH)
                
                if((row + col) % 2 == 0):
                    color = PALE
                    #pygame.draw.rect(screen, WHITE, rect)
                else:
                    color = GREEN
                    #pygame.draw.rect(screen, BLACK, rect)
                
                pygame.draw.rect(screen, color, rect)

    def showPieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                
                if self.board.squares[row][col].hasPiece():
                    piece = self.board.squares[row][col].piece
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQUARE_WIDTH + (SQUARE_WIDTH // 2), row * SQUARE_HEIGHT + (SQUARE_HEIGHT // 2) 

                    piece.texture_rect = img.get_rect(center=img_center)
                    screen.blit(img, piece.texture_rect)

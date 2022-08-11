import math
import os

class Piece:
    def __init__(self, rank, color, value, texture=None, textureRect=None):
        self.rank = rank
        self.color = color
        
        if color == 'white':
            value_sign = 1
        else:
            value_sign = -1
        self.value = value * value_sign
       
        self.moves = []
        self.moved = False

        self.texture = texture
        self.set_texture()
        self.textureRect = textureRect

    def set_texture(self, size = 80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.rank}.png'
        )    

    def add_moves(self, move):
        self.moves.append(move)

class Pawn(Piece):
    def __init__(self, color):
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
        
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, math.inf)
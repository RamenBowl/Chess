#CONSTANTS
PAWN = 0
ROOK = 1
KNIGHT = 2
BISHOP = 3
QUEEN = 4
KING = 5

WHITE = 0
BLACK = 1

class Piece:
    def __init__(self, rank, color):
        self.rank = rank
        self.color = color

    def getPieceRank(self):
        if self.rank == PAWN:
            return "P"
        elif self.rank == ROOK:
            return "R"
        elif self.rank == KNIGHT:
            return "k"
        elif self.rank == BISHOP:
            return "B"
        elif self.rank == QUEEN:
            return "Q"
        else:
            return "K"


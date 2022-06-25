from Piece import Piece

#CONSTANTS
PAWN = 0
ROOK = 1
KNIGHT = 2
BISHOP = 3
QUEEN = 4
KING = 5

WHITE = 0
BLACK = 1

PAWNS = 8
ROOKS = 2
KNIGHTS = 2
BISHOPS = 2
QUEENS = 1
KINGS = 1

ROWS = 8
COLS = 8

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        
        for i in range(PAWNS):
            self.board[1][i] = Piece(PAWN, WHITE)
            self.board[6][i] = Piece(PAWN, BLACK)

        for i in range(ROOKS):
            self.board[0][i*7] = Piece(ROOK, WHITE)
            self.board[7][i*7] = Piece(ROOK, BLACK)
        
        for i in range(KNIGHTS):
            self.board[0][i*5 + 1] = Piece(KNIGHT, WHITE)
            self.board[7][i*5 + 1] = Piece(KNIGHT, BLACK)

        for i in range(BISHOPS):
            self.board[0][i*3 + 2] = Piece(BISHOP, WHITE)
            self.board[7][i*3 + 2] = Piece(BISHOP, BLACK)
        
        self.board[0][3] = Piece(QUEEN, WHITE)
        self.board[7][3] = Piece(QUEEN, BLACK)
        
        self.board[0][4] = Piece(KING, WHITE)
        self.board[7][4] = Piece(KING, BLACK)

    def printBoard(self):
        s = ""
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] == None:
                    s = s + " * "
                else:
                    s = s + " " + self.board[i][j].getPieceRank() + " "
            print(s)
            s = ""

    def printBoardRow(self, rowNum):
        s = ""
        for j in range(COLS):
            if self.board[rowNum][j] == None:
                s = " * " + s
                print(" * ")
            else:
                s = " " + self.board[rowNum][j].getPieceRank() + " " + s
                print(" " + self.board[rowNum][j].getPieceRank() + " ")
        print(s)


    def locValid(self, loc):
        (x,y) = loc
        if 0 <= x and x <=7 and 0 <= y and y <= 7:
            return True
        return False
    
    def isPawnMoveValid(self, startLoc, stopLoc):
        return False

    def isRookMoveValid(self, startLoc, stopLoc):
        return False

    def isKnightMoveValid(self, startLoc, stopLoc):
        return False

    def isBishopMoveValid(self, startLoc, stopLoc):
        return False

    def isQueenMoveValid(self, startLoc, stopLoc):
        return False

    def isKingMoveValid(self, startLoc, stopLoc):

    def isMoveValid(self, startLoc, stopLoc):
        (x1, y1) = startLoc
        (x2, y2) = stopLoc

        if not locValid(startLoc) or not locValid(stopLoc):
            return False
        
        if self.board[x1][y1] == None:
            return False




    
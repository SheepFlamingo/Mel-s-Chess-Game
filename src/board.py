from const import *
from square import Square
from piece import *

class Board:
    
    def __init__(self):
        """Creating a list of eight 0s for each column aka creating a 2D array. 
        initalizes the board, and the white and black pieces.
        """
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)]
        
        self.create()
        self.add_pieces('white')
        self.add_pieces('black')
    
    def create(self):
        """Looping through the 2D array to add a square object to the board instead of a zero. """
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col) # Creates a board full of square objects 
    
    def add_pieces(self, color):
        """add pieces to the board. Two rows dedicated to pawns and another two rows dedicated to other pieces

        Args:
            color (str): color of the piece to add to the board
        """
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        
        # Creates all pawns on the chess board
        for col in range(cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        
        # Creates all knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        # Creates all bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        
        #Creates all rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        
        # Creates all Queens
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        
        # Creates all Kings
        self.squares[row_other][4] = Square(row_other, 4, King(color))
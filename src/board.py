from const import *
from square import Square

class Board:
    
    def __init__(self):
        """Creating a list of eight 0s for each column aka creating a 2D array. """
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)]
        
        self.create()
    
    def create(self):
        """Looping through the 2D array to add a square object to the board instead of a zero. """
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col) # Creates a board full of square objects 
    
    def addPieces(self, color):
        pass
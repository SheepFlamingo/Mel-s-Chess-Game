import unittest
from src.square import Square
from src.const import *
from src.piece import *

class TestSquare(unittest.TestCase):
    def test_has_piece_empty_square(self):
        # Test an empty square
        square = Square(3, 3)
        self.assertFalse(square.has_piece())  # Expecting False because middle square is empty in beggining of the game
    
    def test_has_piece_with_piece(self):
        # Test a square with a piece
        piece = Pawn('white')
        square = Square(6, 0, piece)
        self.assertTrue(square.has_piece())  # Expecting True since there's a pawn on the square in the beggining of the game

if __name__ == '__main__':
    unittest.main()
        
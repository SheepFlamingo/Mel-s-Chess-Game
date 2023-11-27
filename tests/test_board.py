import unittest
from src.const import *
from src.square import Square
from src.board import Board
from src.piece import Pawn, Knight, Bishop, Rook, Queen, King

class TestBoard(unittest.TestCase):
    def setUp(self):
        # Create a new board instance for each test
        self.board = Board()
    
    def test_board_creation(self):
        # Check if the board is initalized with the correction number of rows and columns
        self.assertEqual(len(self.board.squares), rows)
        self.assertEqual(len(self.board.squares[0]), cols)
    
    def test_pawn_placement(self):
        # Pawns should only be placed on the first and sixth rows at the beginning of the game 
        row = 1  
        for col in range(cols):
            with self.subTest(f"Checking pawn at row {row}, column {col}"): #The use of self.subTest is helpful for pinpointing exactly which column caused a failure if the test fails.
                square = self.board.squares[row][col]
                self.assertIsInstance(square.piece, Pawn)
        
        row = 6  
        for col in range(cols):
            with self.subTest(f"Checking pawn at row {row}, column {col}"):
                square = self.board.squares[row][col]
                self.assertIsInstance(square.piece, Pawn)
    
    def test_piece_placement(self):
        # Check if the correct pieces are placed on the board
        
        # Knights
        self.assertIsInstance(self.board.squares[0][1].piece, Knight)
        self.assertIsInstance(self.board.squares[0][6].piece, Knight)
        self.assertIsInstance(self.board.squares[7][1].piece, Knight)
        self.assertIsInstance(self.board.squares[7][6].piece, Knight)
        
        # Bishops
        self.assertIsInstance(self.board.squares[0][2].piece, Bishop)
        self.assertIsInstance(self.board.squares[0][5].piece, Bishop)
        self.assertIsInstance(self.board.squares[7][2].piece, Bishop)
        self.assertIsInstance(self.board.squares[7][5].piece, Bishop)
        
        # Rooks
        self.assertIsInstance(self.board.squares[0][0].piece, Rook)
        self.assertIsInstance(self.board.squares[0][7].piece, Rook)
        self.assertIsInstance(self.board.squares[7][0].piece, Rook)
        self.assertIsInstance(self.board.squares[7][7].piece, Rook)
        
        # Queens
        self.assertIsInstance(self.board.squares[0][3].piece, Queen)
        self.assertIsInstance(self.board.squares[7][3].piece, Queen)
        
        # Kings
        self.assertIsInstance(self.board.squares[0][4].piece, King)
        self.assertIsInstance(self.board.squares[7][4].piece, King)
    
    def test_square_objects(self):
        # Check if each element in the board is a Square object
        for row in self.board.squares:
            for square in row:
                self.assertIsInstance(square, Square)

if __name__ == '__main__':
    unittest.main()
                
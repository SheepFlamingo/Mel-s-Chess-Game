import unittest
import os
from src.piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King

class TestPieces(unittest.TestCase):
    def test_piece_init(self):
        piece = Piece('test', 'white', 1.0)
        self.assertEqual(piece.name, 'test')
        self.assertEqual(piece.color, 'white')
        self.assertEqual(piece.value, 1.0)
        self.assertEqual(piece.moves, [])
        self.assertFalse(piece.moved)
        self.assertIsNone(piece.texture)
        self.assertIsNone(piece.texture_rect)

    def test_pawn_init(self):
        pawn_white = Pawn('white')
        pawn_black = Pawn('black')
        
        self.assertEqual(pawn_white.dir, -1)
        self.assertEqual(pawn_black.dir, 1)
        self.assertEqual(pawn_white.value, -1.0)  # Check the value sign for white pawn
        self.assertEqual(pawn_black.value, 1.0)   # Check the value sign for black pawn

    def test_knight_init(self):
        knight = Knight('white')
        self.assertEqual(knight.value, 3.0)

    def test_bishop_init(self):
        bishop = Bishop('white')
        self.assertEqual(bishop.value, 3.001)

    def test_rook_init(self):
        rook = Rook('white')
        self.assertEqual(rook.value, 5.0)

    def test_queen_init(self):
        queen = Queen('white')
        self.assertEqual(queen.value, 9.0)

    def test_king_init(self):
        king = King('white')
        self.assertEqual(king.value, 100_000.0)

    def test_set_texture(self):
        piece = Piece('test', 'white', 1.0)
        piece.set_texture(size=80)
        expected_texture = os.path.join('assets/images/imgs-80px/white_test.png')
        self.assertEqual(piece.texture, expected_texture)

if __name__ == '__main__':
    unittest.main()
import unittest
import pygame
from src.game import Game
from src.const import *
from src.board import Board
from unittest.mock import MagicMock, patch
"""MagicMock is used to create mock objects that allow you to verify if certain methods are called and with what arguments."""

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_show_background(self):
        # MagicMock can be used to mock the pygame.Surface obj
        mock_surface = MagicMock()
        
        # Test show_background method
        self.game.show_background(mock_surface)
        
        # Verify that pygame.draw.rect was called with the correct arguments
        # This assumes a simple 2x2 chessboard pattern
        mock_surface.assert_called_with((234, 235, 200), (0, 0, squareSize, squareSize)) # The top left square is light green
        mock_surface.assert_called_with((119, 154, 88), (squareSize, 0, squareSize, squareSize)) # Next square is dark green
        mock_surface.assert_called_with((119, 154, 88), (0, squareSize, squareSize, squareSize))
        mock_surface.assert_called_with((234, 235, 200), (squareSize, squareSize, squareSize, squareSize))
        
        # Looping through the entire board and checking that pattern is correct
        for row in range(rows):
            for col in range(cols):
                color = (234,235,200) if (row + col) % 2 == 0 else (119,154,88)
                position = (col * squareSize, row * squareSize, squareSize, squareSize)
                mock_surface.assert_called_with(color, position)
        
        
    def test_show_pieces(self):
        mock_surface = MagicMock()
        
        # Test show_pieces method
        # Mock pygame.image.load since loading an actual image may not be necessary for a unit test
        with patch('pygame.image.load', MagicMock(return_value=MagicMock())):
            self.game.show_pieces(mock_surface)
        
        # Assertions for an 8x8 chessboard
        for row in range(rows):
            for col in range(cols):
                square = self.game.board.sqaures[row][col]
                if square.has_piece():
                    piece = square.piece
                    img = pygame.image.load(piece.texture)
                    img_center = col * squareSize + squareSize // 2, row * squareSize + squareSize // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    mock_surface.blit.assert_called_with(img, piece.texture_rect)

if __name__ == '__main__':
    unittest.main()
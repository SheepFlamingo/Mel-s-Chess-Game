import unittest
from unittest.mock import MagicMock, patch
from src.dragger import Dragger
from src.const import *

class TestDragger(unittest.TestCase):
    def setUp(self):
        self.dragger = Dragger()
        
    def test_drag_piece(self):
        piece_mock = MagicMock()
        self.dragger.drag_piece(piece_mock)
        # Checks that the piece is being dragged
        self.assertTrue(self.dragger.dragging)
    
    def test_undrag_piece(self):
        piece_mock = MagicMock()
        self.dragger.piece = piece_mock
        self.dragger.dragging = True
        
        self.dragger.undrag_piece()
        # Expected piece = None, and dragging = False
        self.assertIsNone(self.dragger.piece)
        self.assertFalse(self.dragger.dragging)
    
    def test_save_inital(self):
        pos = (50, 30)
        self.dragger.save_inital(pos)

        expected_row = pos[1] // squareSize
        expected_col = pos[0] // squareSize

        self.assertEqual(self.dragger.initial_row, expected_row)
        self.assertEqual(self.dragger.initial_col, expected_col)
        
    def test_update_mouse(self):
        pos = (50, 30)
        self.dragger.update_mouse(pos)

        self.assertEqual(self.dragger.mouseX, pos[0])
        self.assertEqual(self.dragger.mouseY, pos[1])

    def test_update_blit(self):
        mock_surface = MagicMock()
        mock_texture = MagicMock()

        self.dragger.piece = MagicMock()
        self.dragger.piece.set_texture.return_value = mock_texture

        self.dragger.update_blit(mock_surface)

        mock_texture_rect = MagicMock()
        mock_texture.get_rect.return_value = mock_texture_rect

        mock_surface.blit.assert_called_once_with(mock_texture, mock_texture_rect)


if __name__ == "__main__":
    unittest.main()
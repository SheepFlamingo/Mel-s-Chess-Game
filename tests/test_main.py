import unittest
import pygame
import sys
from unittest.mock import MagicMock, patch
from src.const import *
from src.game import Game
from src.main import Main

class TestGame(unittest.TestCase):
    def test_init(self):
        with patch('pygame.init') as mock_init, \
             patch('pygame.display.set_mode') as mock_set_mode, \
             patch('pygame.display.set_caption') as mock_set_caption:
            
            main = Main()

            # Assertions
            mock_init.assert_called_once()  # Ensure pygame.init is called
            mock_set_mode.assert_called_once_with((width, height))  # Ensure pygame.display.set_mode is called with the correct parameters
            mock_set_caption.assert_called_once_with('Chess')  # Ensure pygame.display.set_caption is called with the correct parameters
            self.assertIsInstance(main.game, Game)  # Ensure that the game attribute is an instance of the Game class

    def test_main_loop(self):
        with patch.object(Main, 'game', MagicMock()) as mock_game, \
             patch('pygame.display.update') as mock_display_update, \
             patch('pygame.quit') as mock_quit, \
             patch('sys.exit') as mock_exit:

            # Mock the return value of pygame.event.get to simulate a QUIT event
            with patch('pygame.event.get', MagicMock(return_value=[MagicMock(type=pygame.QUIT)])):
                main = Main()
                main.main_loop()

                # Assertions
                mock_game.show_background.assert_called_once()  # Ensure show_background is called
                mock_game.show_pieces.assert_called_once()  # Ensure show_pieces is called
                mock_display_update.assert_called_once()  # Ensure pygame.display.update is called
                mock_quit.assert_called_once()  # Ensure pygame.quit is called
                mock_exit.assert_called_once()  # Ensure sys.exit is called

if __name__ == '__main__':
    unittest.main()
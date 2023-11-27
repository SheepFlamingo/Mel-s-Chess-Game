import pygame
from const import *

class Game:
    """Responsible for all the rendering methods aka show methods"""
    def __init__(self):
        pass
    
    def show_background(self, surface):
        """Draw the pattern of the chess board, which follows one dark pattern, then one light pattern.

        Args:
            surface (path): passing self.screen created in the Main class
        """
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) # Light green
                else:
                    color = (119, 154, 88) # Dark green
                    
                rectangle = (col * squareSize, row * squareSize, squareSize, squareSize) # pygame rectangle has 4 params starting from x-axis, then y-axis, finally width and height
                
                pygame.draw.rect(surface, color, rectangle) # Draws the rectangles that make up the chess board
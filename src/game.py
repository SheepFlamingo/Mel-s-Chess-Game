import pygame
from const import *
from board import Board

class Game:
    """Responsible for all the rendering methods aka show methods"""
    def __init__(self):
        self.board = Board()
    
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
    
    def show_pieces(self, surface):
        for row in range(rows):
            for col in range(cols):
                # check if there is a piece on that specific square
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece # Saving that piece onto a variable
                    
                    img = pygame.image.load(piece.texture) # Converts texture into an actual image to be displayed
                    img_center = col * squareSize + squareSize // 2, row * squareSize + squareSize // 2 # Creating an image center to center the piece on the square
                    piece.texture_rect = img.get_rect(center=img_center) # Telling texture_rect the image created to be centered on the square in the display
                    surface.blit(img, piece.texture_rect) # Telling pygame to blit my image into the texture rect which is already centered
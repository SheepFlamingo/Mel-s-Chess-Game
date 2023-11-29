import pygame
from const import *

class Dragger:
    
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        
    def update_blit(self, surface):
        # Setting larger texture
        self.piece.set_texture(size=128)
        
        # Path to the img
        texture = self.piece.texture
        
        # Loading img
        img = pygame.image.load(texture)
        
        # Rect, centering the piece onto the mouse
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        
        # blit img
        surface.blit(img, self.piece.texture_rect)
        
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # Tuple cords (xcord, ycord)
    
    def save_inital(self, pos):
        self.initial_row = pos[1] // squareSize # y coordinate
        self.initial_col = pos[0] // squareSize # x coordinate
    
    def drag_piece(self, piece):
        # Save the piece that is being dragged
        self.piece = piece
        self.dragging = True
    
    def undrag_piece(self):
        self.piece = None
        self.dragging = False

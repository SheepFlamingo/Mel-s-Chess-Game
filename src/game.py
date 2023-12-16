import pygame
from const import *
from board import Board
from dragger import Dragger
from config import Config
from square import Square

class Game:
    """Responsible for all the rendering methods aka show methods"""
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.next_player = 'white'
        self.hovered_sqr = None
        self.config = Config()
    
    def show_background(self, surface):
        """Draw the pattern of the chess board, which follows one dark pattern, then one light pattern.

        Args:
            surface (path): passing self.screen created in the Main class
        """
        # Fill the screen with a background color
        # This clears the screen with a black background color before drawing the chessboard. This prevents the afterimage issue when dragging pieces.
        surface.fill((0, 0, 0))
        
        theme = self.config.theme
        
        for row in range(rows):
            for col in range(cols):
                # color
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                # rect
                rect = (col * squareSize, row * squareSize, squareSize, squareSize) # pygame rectangle has 4 params starting from x-axis, then y-axis, finally width and height
                # blit
                pygame.draw.rect(surface, color, rect)  # Draws the rectangles that make up the chess board
                
                # row coordinates
                if col == 0:
                    # color
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(str(rows-row), 1, color)
                    lbl_pos = (5, 5 + row * squareSize)
                    # blit
                    surface.blit(lbl, lbl_pos)
                    
                # col coordinates
                if row == 7:
                    # color
                    color = theme.bg.dark if (row + col) % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(Square.get_alphacol(col), 1, color)
                    lbl_pos = (col * squareSize + squareSize - 20, height - 20)
                    # blit
                    surface.blit(lbl, lbl_pos)
    
    def show_pieces(self, surface):
        for row in range(rows):
            for col in range(cols):
                # check if there is a piece on that specific square
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece # Saving that piece onto a variable
                    
                    # all pieces except dragger pieces
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture).convert_alpha() # Converts texture into an actual image to be displayed, used .convert_alpha function for efficiency and transparency
                        img_center = col * squareSize + squareSize // 2, row * squareSize + squareSize // 2 # Creating an image center to center the piece on the square
                        piece.texture_rect = img.get_rect(center=img_center) # Telling texture_rect the image created to be centered on the square in the display
                        surface.blit(img, piece.texture_rect) # Telling pygame to blit my image into the texture rect which is already centered

    
    def show_moves(self, surface):
        theme = self.config.theme
        if self.dragger.dragging:
            piece = self.dragger.piece # This is the piece to show the moves

            # Loop all valid moves and blit them
            for move in piece.moves:
                # Color
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                # Rect
                rect = (move.final.col * squareSize, move.final.row * squareSize, squareSize, squareSize)
                # Blit
                pygame.draw.rect(surface, color, rect)
    
    def show_last_move(self, surface):
        theme = self.config.theme
        
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            
            for pos in [initial, final]:
                # Color
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                # Rect
                rect = (pos.col * squareSize, pos.row * squareSize, squareSize, squareSize)
                # Blit
                pygame.draw.rect(surface, color, rect)
    
    def show_hover(self, surface):
        if self.hovered_sqr:
                # Color
                color = (180,180,180)
                # Rect
                rect = (self.hovered_sqr.col * squareSize, self.hovered_sqr.row * squareSize, squareSize, squareSize)
                # Blit
                pygame.draw.rect(surface, color, rect, width=3)
    
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'
    
    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]
    
    def change_theme(self):
        self.config.change_theme()

    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()

    def reset(self):
        self.__init__()
import pygame
import sys
from pygame.locals import *

from const import *
from game import Game


class Main:
    def __init__(self):
        """Initialize pygame, the window for display, and the caption for the window."""
        pygame.init()
        
        # Set up flags for fullscreen and double buffering
        # flags = FULLSCREEN | DOUBLEBUF
        
        # Adjust the display mode to match the screen dimensions and pixel depth
        self.screen = pygame.display.set_mode( (width, height)) # Creates a new window to display the game || , flags, 16 added for fs
        
        pygame.display.set_caption('Chess')
        self.game = Game()
    
    def main_loop(self):
        
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        
        while 1:
            
            # Show Methods
            game.show_background(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)
            
            for event in pygame.event.get():
                
                # Mouse click    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    """
                    Make pieces move
                    What are the events for moving a piece
                    1. Mouse click on a specific piece
                    2. Mouse motion
                    3. Releasing mouse click
                    """
                    dragger.update_mouse(event.pos) # Returns the position of the mouse click on tuple (x,y)
                    
                    
                    clicked_row = dragger.mouseY // squareSize
                    clicked_col = dragger.mouseX // squareSize
                    
                    # Check if clicked position has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.save_inital(event.pos) # This is a save spot incase the player does an invalid move, the method will be implmmented later
                        dragger.drag_piece(piece)

                        # show methods
                        game.show_background(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        
                
                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    # Only want to capture mouse motion when dragging is True
                    if dragger.dragging:
                        # Update mouse position
                        dragger.update_mouse(event.pos)
                        
                        # Keeps background and pieces on screen || Show methods
                        game.show_background(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        
                        # Update blit to piece being moved
                        dragger.update_blit(screen)
                
                # Click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                
                # Check if the user is attempting to quit the application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
    
            pygame.display.update() # Make sure this is the last event in the loop

""" Create an instance of Main, then run the main loop. """
main = Main()
main.main_loop()
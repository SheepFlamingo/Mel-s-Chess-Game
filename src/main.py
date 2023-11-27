import pygame
import sys
from const import *
from game import Game

class Main:
    def __init__(self):
        """Initialize pygame, the window for display, and the caption for the window."""
        pygame.init()
        self.screen = pygame.display.set_mode( (width, height) ) # Creates a new window to display the game
        pygame.display.set_caption('Chess')
        self.game = Game()
    
    def main_loop(self):
        
        game = self.game
        screen = self.screen
        
        while True:
            game.show_background(screen) # Creates a new window to display the board
            game.show_pieces(screen)
            
            for event in pygame.event.get():
                """Running through all of the events to check if the user is attempting to quit the application.""" ,
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            
            
            
            
            
                    
            pygame.display.update() # Make sure this is the last event in the loop

""" Create an instance of Main, then run the main loop. """
main = Main()
main.main_loop()
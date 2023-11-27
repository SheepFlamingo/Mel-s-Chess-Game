import os

class Piece:
    
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        """initalizes a Piece object with their attributes

        Args:
            name (str): name of a piece.
            color (int): color code for the piece
            value (int): all pieces in chess have a value associated with them, which is taken from the offical rules. This will allow for future implmmentation of an AI to evulate moves based on piece value.
            texture (_type_, optional): _description_. Defaults to None.
            teture_rect (_type_, optional): _description_. Defaults to None.
        """
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1 # White pieces will have positive values and black pieces will have negative values which will help the AI differentiate between the two.
        self.value = value * value_sign
        self.moves = [] # The valid moves of a piece
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size=80):
        """path to the assests folder for the texture of the piece

        Args:
            size (int, optional): There is a case for both 128px and 80px. Defaults to 80px.
        """
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )
    
    def add_moves(self, move):
        self.moves.append(move)
    
class Pawn(Piece):
    def __init__(self, color):
        """Coordinates work differently in pygame, because while the x-axis behaves as expected the y-axis increases value going downard and decreases value going upward.
            The game will position the white pieces at the bottom of the screen.
            The game will position the black pieces at the top of the screen.
            
            (Side note: This is fine for now, but should figure out a way to let the player be able to flip the board, and the pawns still know which way to move)
            
        Args:
            color (str): color of the pawn determines its direction.
        """
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        """
        """
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        """
        """
        super().__init__('bishop', color, 3.001) # The value of the bishop is slightly higher than a knight, which will allow the AI to know that they are more important.

class Rook(Piece):
    def __init__(self, color):
        """
        """
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        """
        """
        super().__init__('queen', color, 9.0)

class King(Piece):
    def __init__(self, color):
        """
        """
        super().__init__('king', color, 100_000.0) # The king is the most valuable piece in the game, this will tell the AI you cannot lose it or you will lose the game if this doesn't work we can change it to math.infinity, but the reason I chose a concrete number is to make it more efficicent.



class Square:
    
    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    
    def __init__(self, row, col, piece=None):
        """Initalizing a square with either a piece or leaving it as an empty square.

        Args:
            row (int): Range 0 to 7
            col (int): Range 0 to 7
            piece (self, optional): A piece to be initalized from the piece class. Defaults to None.
        """
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol = self.ALPHACOLS[col]
    
    def __eq__(self, other):
        #Dunder method to tell python when does a move equal to another move
        return self.row == other.row and self.col == other.col
    
    def has_piece(self):
        """Checks if this square has a piece.
        
        Returns:
            True if this square has a piece
            False if this square doesn't have a piece
        """
        return self.piece != None
    
    def isempty(self):
        # Checking if space is empty
        return not self.has_piece()
    
    def has_team_piece(self, color):
        # Checking is space is occupied with a team piece
        return self.has_piece() and self.piece.color == color

    def has_rival_piece(self, color):
        # Checking if the space is occupied with a rival team piece
        return self.has_piece() and self.piece.color != color

    def isempty_or_rival(self, color):
        # Checking if the space is empty or has a rival piece
        return self.isempty() or self.has_rival_piece(color)

    @staticmethod
    def in_range(*args): # *args = lists of arguements
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        
        return True
    
    @staticmethod
    def get_alphacol(col):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHACOLS[col]

class Square:
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
    
    def has_piece(self):
        """Checks if this square has a piece.
        
        Returns:
            True if this square has a piece
            False if this square doesn't have a piece
        """
        return self.piece != None
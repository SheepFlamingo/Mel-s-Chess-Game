from const import *
from square import Square
from piece import *
from move import Move

class Board:
    
    def __init__(self):
        """Creating a list of eight 0s for each column aka creating a 2D array. 
        initalizes the board, and the white and black pieces.
        """
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)]
        
        self.create()
        self.add_pieces('white')
        self.add_pieces('black')
    
    def calc_moves(self, piece, row, col):
        """ Responisble for calculating all the valid moves of a specific piece on a specific position
        """
        def pawn_moves():
            # On the pawn's first turn they can move 2 squares, otherwise they can only move 1 square
            steps = 1 if piece.moved else 2

            # Vertial moves
            start = row + piece.dir 
            end = row + (piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # Create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # Create a new move
                        move = Move(initial, final)
                        # Append new move
                        piece.add_move(move)
                    # This means the pawn is blocked from moving forward
                    else: break
                # The move is not in range
                else: break

            # Diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col - 1, col + 1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                        # Create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create a new move
                        move = Move(initial, final)
                        # Append new move
                        piece.add_move(move)
            #Promotion

            #En Passant
    
        def knight_moves():
            # 8 Possible moves
            possible_moves = [
                (row - 2, col + 1),
                (row - 2, col - 1),
                (row - 1, col + 2),
                (row - 1, col - 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col + 2),
                (row + 1, col - 2)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # Create the squares of the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece=piece
                        # Create a new move
                        move = Move(initial, final)
                        piece.add_move(move) # Append new valid move

        def striaghtline_moves(incrs): #  incrs = increments
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        
                        # Create the squares of the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece=piece
                        # Create a possible new move
                        move = Move(initial, final)

                        # Empty square
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # Append new valid move
                            piece.add_move(move)


                        # Has enemy piece = add move + break
                        if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            # Append new valid move
                            piece.add_move(move)
                            break

                        # Has Team piece = break
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break

                    # Not in range
                    else: break

                    # Incrementing incrs
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def king_moves():
            possible_moves = [
                (row-1, col+0), #Up
                (row-1, col+1), #Up-Right
                (row+0, col+1), #Right
                (row+1, col+1), #Down-Right
                (row+1, col+0), #Down
                (row+1, col-1), #Down-Left
                (row+0, col-1), #Left
                (row-1, col-1) #Up-Left
            ] 
            # Normal Valid Moves
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # Create the squares of the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece=piece
                        # Create a new move
                        move = Move(initial, final)
                        piece.add_move(move) # Append new valid move
            # Short Castling

            # Long Castling

        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            striaghtline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1) # down-left
            ])

        elif isinstance(piece, Rook):
            striaghtline_moves([
                (-1, 0), # Up
                (0, 1), # Right
                (1, 0), # Down
                (0, -1) # Left
            ])

        elif isinstance(piece, Queen):
            striaghtline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # Up
                (0, 1), # Right
                (1, 0), # Down
                (0, -1) # Left
            ])

        elif isinstance(piece, King):
            king_moves()

    def create(self):
        """Looping through the 2D array to add a square object to the board instead of a zero. """
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col) # Creates a board full of square objects 
    
    def add_pieces(self, color):
        """add pieces to the board. Two rows dedicated to pawns and another two rows dedicated to other pieces

        Args:
            color (str): color of the piece to add to the board
        """
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        
        # Creates all pawns on the chess board
        for col in range(cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        
        # Creates all knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        # Creates all bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        
        #Creates all rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        
        # Creates all Queens
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        
        # Creates all Kings
        self.squares[row_other][4] = Square(row_other, 4, King(color))
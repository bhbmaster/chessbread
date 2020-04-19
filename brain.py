# for help w/ classes
# https://www.geeksforgeeks.org/design-a-chess-game/

class Spot:  # also known as squares
    def __init__(self,i,j,x,y,width,height,is_white,piece):
        self.i=i             # i is 0,1,2,3,4,5,6,7 (0 is left most square)
        self.j=j             # j is 0,1,2,3,4,5,6,7 (0 is top most square)
        self.x=i             # x top left x of square
        self.y=y             # y top left y of square
        self.width=width     # width x width
        self.height=height   # height h width
        self.piece=piece     # the Piece()
        self.is_white=is_white        # true if white, false if black
        self.rect=(x,y,width,height)

class Piece: # abstract
    pass

class Pawn(Piece):
    pass

class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

class Board:
    def __init__(self,spot_list=[]):
        self.spot_list = spot_list # list of spots for the board
    def reset_pieces(self):
        # goes thru all of the spots and sets new game
        pass
        
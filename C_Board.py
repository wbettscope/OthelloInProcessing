#<Will Betts Cope>
### BOARD ###

#imports
from B_Square import *

class Board():
    
#Constructor
    def __init__(self, s):
        #preconditions
        assert type(s) is int
        
        self.s = s  #board size (number of squares across)
        self.turn = 'B'
        self.rep = [[Square(0,0,w/s)]*s for i in range(s)]    #initilize s by s empty 2D array
        
        for i in range(s):
            for j in range(s):
                self.rep[i][j] = Square(i*w/s,j*w/s,w/s)    #fill the array with squares

#Board value methods
    
    #returns square on Board at position (x,y)
    def getSquare(self, x, y):
        #preconditions
        assert x <= self.s - 1
        assert y <= self.s - 1

        return self.rep[x][y]
    
#Board size methods

    #returns board size
    def getSize(self):
        return self.s
    
#Piece playing methods

    #play Piece in Square that contains (mouseX, mouseY) and return Square's coordinates on the board
    def playPiece(self, x, y):
        if self.getSquare(x,y).isSelected() and self.getSquare(x,y).getPiece().empty():
            self.getSquare(x,y).getPiece().setVal(self.turn)
            if self.turn == 'B':
                self.turn = 'W'
            elif self.turn == 'W':
                self.turn = 'B'
                
    #return position on board of highlighted square (where move will potentially be made)
    def getHighlightedSq(self):
        for i in range(self.s):
            for j in range(self.s):
                if self.getSquare(i,j).isSelected():
                    return (i,j)
                          
#Board display methods
    
    #displays the board
    def display(self, here = None, there = None):
        #preconditions
        assert here <= self.s - 2 and there <= self.s - 1
        assert here < there or here == None and there <= None
        
        if here == None and there == None:
            for i in range(self.s):
                for j in range(self.s):
                    self.rep[i][j].display()
        else:
            for i in range(there-here):
                for j in range(there-here):
                    self.rep[here+i][here+j].display()

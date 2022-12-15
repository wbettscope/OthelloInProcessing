#<Will Betts Cope>
### SQUARE ###

#imports
from A_Piece import *

class Square():
    
#Constructor
    def __init__(self, x, y, l, val = None):
        #preconditions
        assert x <= w and y <= h
        assert type(val) is Piece or val == None

        self.x = x  #square top left corner x coordinate
        self.y = y  #square top left corner y coordinate
        self.l = l  #square side length
        self.selected = False  #True if mouse is within Square

        if val == None:
            self.rep = Piece(x+l/2,y+l/2,l*6/7) #square representation (piece)
        else:
            self.rep = Piece(x+l/2,y+l/2,l*6/7,val)

#Square value methods

    #returns true iff square's piece is empty
    def empty(self):
        return self.rep.empty()

    #returns Square's piece
    def getPiece(self):
        return self.rep
    
    #returns Square's piece's value
    def getPieceVal(self):
        return self.rep.getVal()
    
    #sets Square's piece's value to passed val
    def setPieceVal(self, val):
        #preconditions
        assert val == 'B' or val == 'W' or val == 'G' or val == '_'

        self.rep.setVal(val)

#Square size methods

    #returns square side length
    def getLen(self):
        return self.l

    #sets square side length to passed l
    def setLen(self, l):
        self.l = l

#Square location methods

    #returns square top left corner x coordinate
    def getX(self):
        return self.x

    #sets square top left corner x coordinate to passed x
    def setX(self, x):
        #preconditions
        assert x <= w

        self.x = x

    #returns square top left corner y coordinate
    def getY(self):
        return self.y

    #sets square top left corner y coordinate to passed y
    def setY(self, y):
        #preconditions
        assert y <= h

        self.y = y
        
#Square selection/highlight methods

    #returns True if mouse is within Square
    def isSelected(self):
        return self.selected

#Square display related methods

    #Displays piece as Square with top left coordinates (x,y) and side length l
    def display(self):
        if mouseX > self.x and mouseX < self.x + self.l and mouseY > self.y and mouseY < self.y + self.l:
            stroke(2,35,2)
            strokeWeight(2)
            fill(200,250,200,50)
            square(self.x,self.y,self.l)
            self.rep.display()
            self.selected = True
        else:
            stroke(2,35,2)
            strokeWeight(2)
            noFill()
            square(self.x,self.y,self.l)
            self.rep.display()
            self.selected = False

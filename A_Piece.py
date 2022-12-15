#<Will Betts Cope>
### PIECE ###

#global variables
w = 900 #screen height
h = 900 #screen width
assert w == h   

class Piece():
    #constructor
    def __init__(self, x, y, r, val = None):
        #preconditions
        assert x <= w and y <= h
        assert val == 'B' or val == 'W' or val == None

        self.x = x  #piece center x coordinate
        self.y = y  #piece center y coordinate
        self.r = r  #piece radius

        if val == None:
            self.rep = '_'  #piece representation (value)
        else:
            self.rep = val

#Piece value methods

    #returns true iff piece is neither black nor white
    def empty(self):
        return self.rep == '_' or self.rep == 'G'

    #returns piece value
    def getVal(self):
        return self.rep
    
    #returns pieve RGB value
    def getValRGB(self):
        if self.rep == 'W':
            return 255
        return 0

    #sets piece value to passed val
    def setVal(self, val):
        #preconditions
        assert val == 'B' or val == 'W' or 'G' #'G' for a ghost piece

        self.rep = val

    #reverses piece color
    def flip(self):
        if self.rep == 'B':
            self.setVal('W')
        elif self.rep == 'W':
            self.setVal('B')

#Piece size methods

    #returns piece radius
    def getRad(self):
        return self.r

    #sets piece radius to passed r
    def setRad(self, r):
        self.r = r

#Piece location methods

    #returns piece center x coordinate
    def getX(self):
        return self.x

    #sets piece center x coordinate to passed x
    def setX(self, x):
        #preconditions
        assert x <= w

        self.x = x

    #returns piece center y coordinate
    def getY(self):
        return self.y

    #sets piece center y coordinate to passed y
    def setY(self, y):
        #preconditions
        assert y <= h

        self.y = y

#Piece display method

    #Displays piece as circle with center (x,y) and radius r
    def display(self):
        if self.rep == 'B':
            stroke(20)
            strokeWeight(2)
            fill(0)
            circle(self.x,self.y,self.r)
        elif self.rep == 'W':
            stroke(225)
            strokeWeight(2)
            fill(255)
            circle(self.x,self.y,self.r)
        elif self.rep == 'G': #Ghost piece (possible move)
            noStroke()
            fill(10,75)
            circle(self.x,self.y,self.r)

#<Will Betts Cope>
### CPU ### 

#imports
from D_Othello import *

class CPU():
    
    displayMove = (0,0) #move to display on the display numbers
    
#Move Methods

    #returns the CPU's move
    def chooseMove(self, game):
        #preconditions
        thisIsForAnAssertion = Othello()
        assert type(game) is type(thisIsForAnAssertion)
        
        potentialMove = game.getMostFlips()
        if game.inLegalMoves((1,1)): #Prioritize corners
            potentialMove = (1,1)
        elif game.inLegalMoves((1,8)):
            potentialMove = (1,8)
        elif game.inLegalMoves((8,1)):
            potentialMove = (8,1)
        elif game.inLegalMoves((8,8)):
            potentialMove = (8,8)
        
        return potentialMove
    
    #displays square numbers for CPU's Move
    def displayNumbers(self, t=None):
        #preconditions
        assert type(t) is tuple or t == None
        
        textSize(26)
        s = 10 #dimentions of the board
        for i in range(s):
            if i != 0 and i != 9 and type(t) is tuple and i == t[0]:
                fill(100,2,2)
                text(i,i*w/s+40,50)
            elif i != 0 and i != 9:
                fill(2,35,2)
                text(i,i*w/s+40,50)
        
        for j in range(s):
            if j != 0 and j != 9 and type(t) is tuple and j == t[1]:
                fill(100,2,2)
                text(j,35,j*w/s+40)
            elif j != 0 and j != 9:
                fill(2,35,2)
                text(j,35,j*w/s+40)
    
    #returns displayMove
    def getDisplayMove(self):
        return self.displayMove
    
    #sets displayMove to passed t
    def setDisplayMove(self,t):
        #preconditions
        assert type(t) is tuple
        
        self.displayMove = t
        
    def noMovesClickHere(self):
        noFill()
        stroke(2,35,2)
        circle(w/10-45,w/10-40,75)
        textSize(18)
        fill(2,35,2)
        text("NO",w/10-60,w/10-47)
        text("MOVES",w/10-75,w/10-27)
        
        

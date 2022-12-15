#<Will Betts Cope>
### OTHELLO ### 

#imports
from C_Board import *

class Othello():
    
#Constructor
    def __init__(self):
        #create board - 10 by 10 for simple move legality checking, only center 8 by 8 displayed
        self.rep = Board(10)
        
        #set 4 starting Pieces
        self.rep.getSquare(4,4).setPieceVal('W')
        self.rep.getSquare(5,5).setPieceVal('W')
        self.rep.getSquare(4,5).setPieceVal('B')
        self.rep.getSquare(5,4).setPieceVal('B')
        
        #piece used to track current turn
        self.turn = Piece(w/2,90,45,'B')
        
        #array used to track current legal moves
        self.legalMoves = []
        
#Turn methods
        
    #flips the piece used to track the current turn
    def flipTurn(self):
        self.turn.flip()
        
    #returns the value of the piece used to track turn
    def getTurnVal(self):
        return self.turn.getVal()

#Legal moves methods
    
    #returns a list of the legal moves
    def getLegalMoves(self):
        self.legalMoves = [] #set legalMoves to empty
        
        #1. loop through board
        for i in range(self.rep.getSize()):
            for j in range(self.rep.getSize()):
                #2. if opponent's piece is found, check for empty sqaures in the 8 surrounding squares
                if self.rep.getSquare(i,j).getPieceVal() != self.turn.getVal() and not self.rep.getSquare(i,j).getPiece().empty():
                    for a in [-1,0,1]:
                        for b in [-1,0,1]:
                            #3. if an empty space is found, find the distance to each edge of the board
                            if self.rep.getSquare(i+a,j+b).getPiece().empty():
                                dDist = self.rep.getSize()-(j+b)-1 #amount of squares to check below
                                rDist = self.rep.getSize()-(i+a)-1 #amount of squares to check to the right
                                lDist = i+a #amount of squares to check to the left
                                uDist = j+b #amount of squares to check above 
                                if (i+a + j+b)//2 <= 4: 
                                    urdDist = uDist #amount of squares to check on the up right diagonal
                                    dldDist = lDist #amount of squares to check on the down left diagonal
                                else:
                                    urdDist = rDist
                                    dldDist = dDist
                                if i+a >= j+b:
                                    uldDist = uDist #amount of squares to check on the up left diagonal
                                    drdDist = rDist #amount of squares to check on the down right diagonal
                                else:
                                    uldDist = lDist
                                    drdDist = dDist
                                distDict = {"dDist":dDist,"rDist":rDist,"lDist":lDist,"uDist":uDist,"urdDist":urdDist,"uldDist":uldDist,"dldDist":dldDist,"drdDist":drdDist}
                                #4. Using those distances, check for outflanks along horizonal, vertical, and diagonal lines, and add square to legal move list if it outflanks an opponent's piece
                                for m in distDict:
                                    outflank = False #used to confirm that an outflank of an opponent's piece is possible for a gieven potential move
                                    outflankLS = [] #list of pieces a potential move would outflank
                                    for n in range(distDict[m]):
                                        if m == 'dDist':
                                            curX = i+a
                                            curY = j+b+n
                                        elif m == 'rDist':
                                            curX = i+a+n
                                            curY = j+b
                                        elif m == 'lDist':
                                            curX = i+a-n
                                            curY = j+b
                                        elif m == 'uDist':
                                            curX = i+a
                                            curY = j+b-n
                                        elif m == 'urdDist':
                                            curX = i+a+n
                                            curY = j+b-n
                                        elif m == 'uldDist':
                                            curX = i+a-n
                                            curY = j+b-n
                                        elif m == 'dldDist':
                                            curX = i+a-n
                                            curY = j+b+n
                                        elif m == 'drdDist':
                                            curX = i+a+n
                                            curY = j+b+n
                                            
                                        #if an empty square is found, stop checking current line
                                        if self.rep.getSquare(curX, curY).getPiece().empty() and n != 0:
                                            break
                                        #if current player's piece is found first, stop checking current line
                                        elif self.rep.getSquare(curX, curY).getPieceVal() == self.turn.getVal() and not outflank:
                                            break
                                        #if opponent's piece is found, confirm that an outflank is possible 
                                        elif self.rep.getSquare(curX, curY).getPieceVal() != self.turn.getVal() and not self.rep.getSquare(curX, curY).getPiece().empty():
                                            outflank = True
                                            outflankLS.append((curX,curY))
                                        #if current player's piece is found, and an outflank is possible, confirm the move in question is legal
                                        elif self.rep.getSquare(curX, curY).getPieceVal() == self.turn.getVal() and outflank and i+a != 0 and i+a != 9 and j+b != 0 and j+b != 9:
                                            for k in outflankLS:
                                                if (i+a, j+b, k) not in self.legalMoves:
                                                    self.legalMoves.append((i+a, j+b, k))
        
    #displays legal moves as ghost pieces
    def displayLegalMoves(self):
        for (i,j,k) in self.legalMoves:
            self.rep.getSquare(i,j).setPieceVal('G')
        
    #hides legal moves
    def hideLegalMoves(self):
        for i in range(self.rep.getSize()):
            for j in range(self.rep.getSize()):
                if self.rep.getSquare(i,j).getPieceVal() == 'G':
                    self.rep.getSquare(i,j).setPieceVal('_')
                    
    #checks if potential move is in legalMoves list
    def inLegalMoves(self,t):
        #preconditions
        assert type(t) is tuple
        
        for (i,j,k) in self.legalMoves:
            if (i,j) == t:
                return True
        return False
    
    #returns True if legalMoves list is empty
    def noLegalMoves(self):
        return len(self.legalMoves) == 0
                    
#Piece flipping methods
    
    #returns number of pieces passed move would flip
    def getFlipNum(self,t):
        #preconditions
        assert type(t) is tuple
        
        flipCount = 0
        for (i,j,k) in self.legalMoves:
            if (i,j) == t:
                flipCount += 1
        
        return flipCount
    
    #returns the move that would flip the most pieces
    def getMostFlips(self):
        mostFlips = (1,1,0)
        for i in range(self.rep.getSize()):
            for j in range(self.rep.getSize()):
                if self.inLegalMoves((i,j)) and self.getFlipNum((i,j)) > mostFlips[2]:
                    mostFlips = (i,j,self.getFlipNum((i,j)))
                elif self.inLegalMoves((i,j)) and self.getFlipNum((i,j)) == mostFlips[2] and random(100) > 49: #if multiple moves flip the same sumber of pieces, only change mostFlips half the time (so the CPU isn't the same every time)
                    mostFlips = (i,j,self.getFlipNum((i,j)))
        return mostFlips
        
    #flip all pieces outflanked by most recent move played
    def flipOutflanked(self,t):
        #preconditions
        assert type(t) is tuple
        
        for (i,j,k) in self.legalMoves:
            if (i,j) == t:
                self.rep.getSquare(k[0],k[1]).getPiece().flip()
                
#Winner detection methods

    #returns a tuple with (a string declaring the color with the most pieces on the board the winner (or a tie), how many pieces they have on the board, how many pieces the opponent has on the board)
    def findWinner(self):
        whiteCount = 0
        blackCount = 0
        
        for i in range(self.rep.getSize()):
            for j in range(self.rep.getSize()):
                if self.rep.getSquare(i,j).getPieceVal() == ('W'):
                    whiteCount += 1
                elif self.rep.getSquare(i,j).getPieceVal() == ('B'):
                    blackCount += 1
                    
        if whiteCount > blackCount:
            return ("White Wins!",whiteCount,blackCount)
        elif blackCount > whiteCount:
            return ("Black Wins!",blackCount,whiteCount)
        else:
            return ("It's a Tie!",whiteCount,blackCount)
                    

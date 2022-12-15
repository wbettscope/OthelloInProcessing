#<Will Betts Cope>
### MAIN ###

#imports
from E_CPU import * 

#global variables
game = Othello() #Instance of current game   
computerPlayer = CPU() #Instance of computer player
playWithCPU = True

def setup():
    size(w,h)
    background(10,50,10)
    
    #find and display legal moves for first turn
    game.getLegalMoves()
    game.displayLegalMoves()
    
    #display the noMovesClickHere instuctions
    computerPlayer.noMovesClickHere()
    
def draw():
    background(10,50,10)
    
    #display the playable area of the board
    game.rep.display(1,9)
    
    if playWithCPU:
        #display CPU's square numbers
        computerPlayer.displayNumbers(computerPlayer.getDisplayMove())
        
    #display the noMovesClickHere instuctions
    computerPlayer.noMovesClickHere()
    
    #display a piece over the mouse to indicate current turn
    fill(game.turn.getValRGB(),100)
    stroke(game.turn.getValRGB(),100)
    circle(mouseX,mouseY,w/10*6/7)
    
def mouseClicked():
    potentialMove = game.rep.getHighlightedSq()
    possibleWin = False
    if game.noLegalMoves():
        possibleWin = True
        game.flipTurn()
    if possibleWin and game.noLegalMoves():
        winner = game.findWinner()
        fill(60,0,100,150)
        rect(w/2-375,h/2-100,750,200,60)
        fill(255)
        textSize(65)
        text(winner[0] + ' ' + str(winner[1]) + ' : ' + str(winner[2]),w/2-280,h/2+15)
        noLoop()
    elif type(potentialMove) is tuple and game.inLegalMoves(potentialMove):
        game.hideLegalMoves()
        game.rep.playPiece(potentialMove[0],potentialMove[1])
        game.flipOutflanked(potentialMove)
        game.flipTurn()
        game.getLegalMoves()
        game.displayLegalMoves()
        if game.getTurnVal() == 'W':
            CPUMove = computerPlayer.chooseMove(game)
            computerPlayer.setDisplayMove(CPUMove)
        elif game.getTurnVal() == 'B':
            computerPlayer.setDisplayMove((0,0))
 
def keyReleased():
    #press any key to turn off CPU
    global playWithCPU
    playWithCPU = not playWithC

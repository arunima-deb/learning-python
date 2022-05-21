# 0 - Empty
# 1 - Cross
# 2 - Knot
# Cross goes first

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

OFFSET = "   "

def printBoard():
    rowNum = 0
    print()
    print( OFFSET, "    a   b   c" )
    print( OFFSET, "  +---+---+---+" )
    while rowNum < len(board):
        row = board[ rowNum ]
        colNum = 0
        
        print( OFFSET, (rowNum+1), "| ", end="" )
        
        while colNum < len( row ):
            colVal = 'E'
            if row[colNum] == 0:
                colVal = ' '
            elif row[colNum] == 1:
                colVal = 'X'
            elif row[colNum] == 2:
                colVal = 'O'

            print( colVal, sep="", end=" | " )
            colNum += 1
        rowNum += 1
        print( "\n", OFFSET, " +---+---+---+" )

def getUserInput( turn ):
    if turn%2 == 1:
        prompt = "\nEnter where you want to place X : "
    else:
        prompt = "\nEnter where you want to place O : "
    move = input( prompt )
    return move
    
def loopGame():
    turn = 1
    while True:                
        printBoard()
        userInput = getUserInput( turn )
        turn += 1   

loopGame()
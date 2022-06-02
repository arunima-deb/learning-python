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

def getCoordinates( move ):
    print(  )
    
    
def loopGame():
    turn = 1
    while True:                
        printBoard()

        # Depending upon the turn, show the appropriate
        # prompt, get the user input and store it in
        # a variable called userInput
        #
        # NOTE: User input can be of type <abc><123>
        #       For example, a1, b2, a3 etc.
        userInput = getUserInput( turn )

        # Convert the user input into x,y board coordinates
        # For example, b1 = row 0, column 1 = (0,1)
        coordinate = getCoordinates( userInput )
        print( "User entered ", coordinate )
        
        turn += 1


loopGame()

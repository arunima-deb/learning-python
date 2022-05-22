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

def getUserInput( player ):
    if player == 1:
        prompt = "\nEnter where you want to place X : "
    else:
        prompt = "\nEnter where you want to place O : "
    move = input( prompt )
    return move

def getBoardCoordinate( move ):
    # move is a 2-character string
    # first char = column (a, b, c)
    # second char = row (1, 2, 3)
    columnChar = move[0]
    colNum = 999999
    if columnChar == 'a':
        colNum = 0
    elif columnChar == 'b':
        colNum = 1
    elif columnChar == 'c':
        colNum = 2
        
    rowChar = move[1]
    rowNum = 999999
    if rowChar == '1':
        rowNum = 0
    elif rowChar == '2':
        rowNum = 1
    elif rowChar == '3':
        rowNum = 2

    coordinates = [colNum, rowNum]    
    return coordinates

def updateBoard( coordinates, player ):
    rowNum = coordinates[1]
    colNum = coordinates[0]
    if player == 1:
        board[rowNum][colNum] = 1
    else:
        board[rowNum][colNum] = 2

def checkWin( player ):
# return values:
# Game still on = 0
# X wins = 1
# O wins = 2
# Draw = 3
    if board[0][0] == player:
        if board[0][1] == player:
            if board[0][2] == player:
                if player == 1:
                    print( 'X wins!!' )
                else:
                    print( 'O wins!!' )
    
def getCurrentPlayer( turn ):
    if turn%2 == 1:
        return 1
    else:
        return 2
        
def loopGame():
    turn = 1
    while True:                
        printBoard()
        player = getCurrentPlayer( turn )
        userInput = getUserInput( player )
        coordinates = getBoardCoordinate( userInput )
        updateBoard( coordinates, player )
        checkWin( player )
        turn += 1

loopGame()

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

def getMove( player ):
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

def makeMove( player, coordinates ):
    rowNum = coordinates[1]
    colNum = coordinates[0]
    if player == 1:
        board[rowNum][colNum] = 1
    else:
        board[rowNum][colNum] = 2

def checkWinRow( player, rowNum ):
    if board[rowNum][0] == player:
        if board[rowNum][1] == player:
            if board[rowNum][2] == player:
                return True
    return False

def checkWinCol( player, colNum ):
    if board[0][colNum] == player:
        if board[1][colNum] == player:
            if board[2][colNum] == player:
                return True
    return False

def checkWinLeftDiagonal( player ):
    if board[0][0] == player:
        if board[1][1] == player:
            if board[2][2] == player:
                return True
    return False

def checkWinRightDiagonal( player ):
    if board[0][2] == player:
        if board[1][1] == player:
            if board[2][0] == player:
                return True
    return False

def checkDraw():
    # returns true if there are no possible moves
    # False otherwise
    if 0 in board[0]:
        return False
    
    elif 0 in board[1]:
        return False

    elif 0 in board[2]:
        return False

    else:
        return True

def checkWin( player, coordinates ):
# return values:
# X wins = 1 [done]
# O wins = 2 [done]
# Draw = 3
# Game still on = 0
    rowNum = coordinates[1]
    colNum = coordinates[0]

    if checkWinRow( player, rowNum ):
        if player == 1:
            print( '\nX wins!!' )
        else:
            print( '\nO wins!!' )
        
        return player
    
    elif checkWinCol( player, colNum):
        if player == 1:
            print( '\nX wins!!' )
        else:
            print( '\nO wins!!' )

        return player
    
    elif checkWinLeftDiagonal( player ):
        if player == 1:
            print( '\nX wins!!' )
        else:
            print( '\nO wins!!' )

        return player
        
    elif checkWinRightDiagonal( player ):
        if player == 1:
            print( '\nX wins!!' )
        else:
            print( '\nO wins!!' )

        return player           

    elif checkDraw():
        return 3
    
    return 0


    
 
    
def getCurrentPlayer( turn ):
    if turn%2 == 1:
        return 1
    else:
        return 2
        
def loopGame():
    turn = 1
    printBoard()
    while True:                
        player = getCurrentPlayer( turn )
        userMove = getMove( player )
        coordinates = getBoardCoordinate( userMove )
        makeMove( player, coordinates )
        printBoard()
        winTrue = ( checkWin( player, coordinates ) )
        if winTrue == player:
            return
        elif winTrue == 3:
            print( 'Draw' )
            return        
        turn += 1
        

loopGame()

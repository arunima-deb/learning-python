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
PLAYER_X = 1
PLAYER_O = 2
EMPTY_CELL = 0

GAME_DRAW = 3
GAME_ON = 0
GAME_X_WIN = PLAYER_X
GAME_O_WIN = PLAYER_O


# Prints the board in its current state
#
#        a   b   c
#      +---+---+---+
#    1 |   |   |   | 
#      +---+---+---+
#    2 |   |   |   | 
#      +---+---+---+
#    3 |   |   |   | 
#      +---+---+---+
#
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

# Based on the player, gets the move from the console
# after displaying proper prompt
def getMove( player ):
    if player == PLAYER_X:
        prompt = "\nEnter where you want to place X : "
    else: 
        prompt = "\nEnter where you want to place O : "
    move = input( prompt )
    return move


# move is a 2-character string
# first char = column (a, b, c)
# second char = row (1, 2, 3)
def getBoardCoordinate( move ):
    columnChar = move[0]
    colNum = ord( columnChar ) - ord( 'a' )
        
    rowChar = move[1]
    rowNum = ord( rowChar ) - ord( '1' )

    coordinates = [colNum, rowNum]
    if colNum < 0 or colNum > 2 or rowNum < 0 or rowNum > 2:
        raise Exception( "Invalid move!" )
        
    return coordinates

# For the given player, marks the given coordinate with the
# sign for the player.
#
# If the coordinate is already occupied, this function throws
# a value error
def makeMove( player, coordinates ):
    rowNum = coordinates[1]
    colNum = coordinates[0]
    if board[rowNum][colNum] == EMPTY_CELL:
        board[rowNum][colNum] = player
    else:
        raise Exception( "Board is already occupied!" )

# Checks if the same player has occupied the entire given row
# if entire row is occupied by same player, the function
# returns True, else False
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

# returns true if there are no possible moves False otherwise
def checkDraw():
    if EMPTY_CELL in board[0]:
        return False
    elif EMPTY_CELL in board[1]:
        return False
    elif EMPTY_CELL in board[2]:
        return False
    else:
        return True

#
# Parameters:
#   player -
#   coordinate -
#
# Return values:
# X wins = GAME_X_WIN
# O wins = GAME_O_WIN
# Draw   = GAME_DRAW
# Game still on = GAME_ON
def checkWin( player, coordinates ):
    rowNum = coordinates[1]
    colNum = coordinates[0]

    if ( checkWinRow( player, rowNum ) or
         checkWinCol( player, colNum ) or
         checkWinLeftDiagonal( player ) or
         checkWinRightDiagonal( player ) ) :
        
        if player == PLAYER_X:
            print( '\nX wins!!' )
        else:
            print( '\nO wins!!' )
        
        return player           

    elif checkDraw():
        return GAME_DRAW
    
    return GAME_ON

# Based on the turn, this function determines who the current player is
# First move is always for cross
def getCurrentPlayer( turn ):
    if turn%2 == 1:
        return 1
    else:
        return 2

# This is the main loop         
def loopGame():
    turn = 1
    printBoard()
    while True:
        try:
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
        except Exception as e:
            print( "\nError:", str( e ) )
        

loopGame()

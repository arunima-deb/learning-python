# ----------------- Change log -------------------------------
# * [DONE] On winning program should display the entire word
#   in the blanks and say 'You win!'
#
# * [DONE] Print the hangman with the completed word after a
#   win or a loss.
#
# * [DONE] If a guess is entered, which has been previously
#   entered let the user know and don't consider the guess
#
# * [DONE] While the game is in progress, user can enter 'new'
#   or 'exit' at the guess prompt to either start a new game
#   or abandon the current game.
#
# * [DONE] After game ends, a prompt should be displayed to
#   either start a new game or exit the program. The default
#   should be to exit.
#       '>> (new | [exit]) :'
#
# * [DONE] Displays incorrect guesses, and guesses remaining
#
# * [DONE] Recognizes and declines invalid guesses.
#    - Strings with more than one character
#    - Non character input
#
# * [DONE] Difficulty level
#     - [DONE] Gather user choice for difficulty level
#     - [DONE] Determines length of word chosen
#     - [DONE] Number of max hints
#
# version 2.0 changes
# ------------------------------------------------------------
# * Gamemodes: A different list of words is inputted for
#   different modes. e.g. Animals, Countries, Historians
#
# * Every game in difficulty level 1 and 2 should provide
#   one letter revealed by default
#
# * Meaning of the word should be revealed at the end
#
# ------------------------------------------------------------

import random
import math

# Data/Variables
words = []
selectedWord = 'Q'

row4 = ( '|          ', '|        O' )
row5 = ( '|          ', '|       /', '|       /|', '|       /|\\' )
row6 = ( '|          ', '|       /', '|       / \\' )

selectedWordLetters = []
blankIndicators = []
currentWordState = []

numIncorrectGuesses = 0
allGuesses = []
correctGuesses = []
incorrectGuesses = []
abandonCurrentGame = False
difficultyLevel = 2

numHintsLeft = 0

# Cleans the state of the current game, so that a new game can
# have a clean start
def cleanGameState():
    global words
    global selectedWordLetters
    global currentWordState
    global numIncorrectGuesses
    global allGuesses
    global correctGuesses
    global abandonCurrentGame
    global incorrectGuesses
    global difficultyLevel
    global numHintsLeft

    words = []
    selectedWordLetters = []
    blankIndicators = []
    currentWordState = []
    numIncorrectGuesses = 0
    allGuesses = []
    correctGuesses = []
    incorrectGuesses = []
    abandonCurrentGame = False
    difficultyLevel = 2
    numHintsLeft = 0

# Loads a list of words from a text file. This function assumes
# that each line of the file is a word. If a line is empty or
# contains a single character, the line is ignored.
def loadDictionary():
    global words
    
    file = open( "hangman-words.txt" )
    for line in file:
        word = line.strip()
        if( word=="" or len(word)==1 ):
            continue
        else:
            words.append( word )

# Selects a word at random from the universal set of words.
def selectWord():
    global selectedWord

    while True:
        ranNum = int(random.randint(0, len(words)))
        selectedWord = words[ranNum]
        selWordLen = len( selectedWord )

        if difficultyLevel == 1 and selWordLen <= 5:
            break
        elif difficultyLevel == 2 and selWordLen < 8:
            break
        elif difficultyLevel == 3 and selWordLen >= 8:
            break        
            
# Prints banner and instructions
def printBanner():
    print( ' _    _                                                  __        ___  ' )
    print( '| |  | |                                                /_ |      / _ \ ' )
    print( '| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |' )
    print( "|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |" )
    print( '| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |' )
    print( '|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ ' )
    print( '                     __/ |                                              ' )
    print( '                    |___/                                               ' )
    print( '\n\nWelcome to Hangman v1.0!                                            ' )
    print( '* Enter exit to abandon round and new to start a new round.             ' )

# Prints hangman in his current state
# the rows that contain hangman's body are variables
# that change according to number of incorrect guesses
def printHangman():

    rowIndexes = [[0,0,0], [1,0,0], [1,1,0], [1,2,0], [1,3,0], [1,3,1], [1,3,2]]
    
    print( '\n ________ ' )
    print( '|        |' )
    print( '|        |' )
    print( '|        |' )

    rowIndexList = rowIndexes[numIncorrectGuesses]
    print( row4[rowIndexList[0]] )
    print( row5[rowIndexList[1]] )
    print( row6[rowIndexList[2]] )

    print( '|        ' )
    print( '|_________________' )
    print( '\n' )
    
    printCurrentWordState()
    if numHintsLeft > 0:
        print( "\n\nNumber of hints =", numHintsLeft )
    else:
        print( '' )

    if numIncorrectGuesses > 0:
        print( '\nIncorrect guesses :', incorrectGuesses )

# Creates a challenge from the selected word by
# removing some or all alphabets
def createChallenge():
    global selectedWordLetters
    global blankIndicators
    global currentWordState
    global selectedWord
    random = 0

    for c in selectedWord:
        selectedWordLetters.append(c)
        blankIndicators.append( 0 )
        currentWordState.append( '_' )

# Prints only the letters of the selected word in their respective places
# according to the user's guesses. Correct guess are printed, while
# pending guesses are shown in [ ]
def printCurrentWordState():
    # print( selectedWord )
    for index in range( 0, len(selectedWord) ):
        if blankIndicators[index] == 0:
            print( '[', currentWordState[index], ']', sep='', end=' ')
        else:
            print( currentWordState[index], end=' ')

# This function receives the guessed letter and updates the
# current word state if the guessed letter belongs to the selected
# word.
#
# If a match is found, this function returns True, else False
def processGuess( guess, humanGuess ):
    global selectedWordLetters
    global blankIndicators
    global currentWordState
    global allGuesses
    global numIncorrectGuesses
    global incorrectGuesses

    matchFound = False
    
    if guess in allGuesses:
        print( guess, 'is already guessed. Try again.' )
        print( (6-numIncorrectGuesses), 'guesses remaining.' )
        return
    else:
        allGuesses.append(guess)
        for i in range( len(selectedWordLetters) ):
            if( blankIndicators[i] == 0 and
                currentWordState[i] == '_' ):
                if( selectedWordLetters[i] == guess ):
                    matchFound = True
                    currentWordState[i] = guess
                    correctGuesses.append(guess)
                
    if( matchFound == False ):
        numIncorrectGuesses += 1
        incorrectGuesses.append(guess)
        print( 'Incorrect!', (6-numIncorrectGuesses), 'guesses remaining.')
    elif humanGuess:
        print( 'Correct!' )
        
    return

# Checks if the user's last move completed the game and if so, print the
# appropriate ending message and return true, else return false.
#
# A game is completed when:
#     i) All blanks are filled
#    ii) Number of incorrect guesses exceeds the maximum number of guesses
def isGameOver():
    global blankIndicators
    global currentWordState
    global selectedWordLetters
    global abandonCurrentGame

    if abandonCurrentGame == True:
        return True

    isLastMove = False
    
    if len(set(correctGuesses)) == len(set(selectedWordLetters)):
        printHangman()
        print( "\n\nYou win!" )
        # TODO: mention keys to exit, start new game, etc. etc.
        isLastMove = True

    if numIncorrectGuesses == 6:
        print( "\n\nYou lose..." )
        currentWordState = selectedWordLetters
        for index in range( 0, len(blankIndicators) ):
            blankIndicators[index] = 0
        printHangman()
        isLastMove = True

    return isLastMove

# Collects difficulty level, game mode and other data
def getGameConfig():
    global difficultyLevel

    while True:
        prompt = "Enter a difficulty level ( 1/[2]/3 ) : "
        userInput = input( prompt )

        if( userInput != "" and not userInput.isdigit() ):
             print( "  Please enter a valid difficulty level" )
        else:
            difficultyLevel = 2 if userInput == "" else int(userInput)
            if userInput == '':
                print( "  Setting difficulty level to default [2]." )
            if difficultyLevel >= 1 and difficultyLevel <=3:
                break
            else:
                print( "  Please enter a valid difficulty level" )

# Determines number of hints according to difficulty level
def determineNumHints():
    global numHintsLeft

    hintPct = 0.5
    match difficultyLevel:
        case 1:
            hintPct = 0.2
        case 2:
            hintPct = 0.25
        case 3:
            hintPct = 0.3

    numHintsLeft = math.ceil( hintPct * len(selectedWord) )

# Returns a random character from the set of characters of the
# selected word, which have not been input by the user yet
def pickHint():
    global selectedWordLetters
    global correctGuesses
    remainingGuesses = []

    for c in selectedWordLetters:
        if c not in correctGuesses and c not in remainingGuesses:
            remainingGuesses.append( c )
      
    ranNum = random.randint(0, len(remainingGuesses)-1)
    guess = remainingGuesses[ranNum]
 
    return str(guess)
            
def main():
    global abandonCurrentGame
    global numHintsLeft
    
    print( '\n\n' )

    cleanGameState() 
    printBanner()
    getGameConfig()
    loadDictionary()
    selectWord()
    createChallenge()
    determineNumHints()
  
    while not isGameOver():
        printHangman()
        guess = input( '\n\n>> ' )       
        humanGuess = True
        
        if guess == 'exit':
            print( '\nGame abandoned' )
            abandonCurrentGame = True
        elif guess == 'new':
            main()
            return
        elif guess == 'hint':
            if numHintsLeft <= 0:
                print( "\nUser has exhausted their supply of hints!" )
                continue
            else:
                numHintsLeft -= 1
                guess = pickHint()
                humanGuess = False
                print( "\nHint =", guess, ". Number of hints remaining = ", numHintsLeft )

        if len( guess ) != 1 or guess.isdigit():
            print( 'Please enter a valid guess.' )
        else:
            processGuess( guess[0], humanGuess )

    guess = input( '>> (new \ [exit]) : ' )
    if guess == 'new':
        main()
    else:
        return
        
main()

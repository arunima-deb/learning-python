import random

# Data/Variables
words = []
selectedWord = 'Q'

row4 = ( '|          ', '|        O' )
row5 = ( '|          ', '|       /', '|       /|',
                '|       /|\\' )
row6 = ('|          ', '|       /', '|       / \\' )

selectedWordLetters = []
blankIndicators = []
currentWordState = []

incorrectGuesses = 0
correctGuesses = []


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

def selectWord():
    global selectedWord
    
    ranNum = int(random.randint(0, len(words)))
    selectedWord = words[ranNum]

    
        
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
    print( '\n\nWelcome to Hangman v1.0!\nEnter exit to abandon round and new to start a new round.' )  

# Prints hangman in his current state
# the rows that contain hangman's body are variables
# that change according to number of incorrect guesses
def printHangman():

    rowIndexes = [[0,0,0], [1,0,0], [1,1,0], [1,2,0], [1,3,0], [1,3,1], [1,3,2]]
    
    print( '\n ________ ' )
    print( '|        |' )
    print( '|        |' )
    print( '|        |' )

    rowIndexList = rowIndexes[incorrectGuesses]
    print( row4[rowIndexList[0]] )
    print( row5[rowIndexList[1]] )
    print( row6[rowIndexList[2]] )

    print( '|        ' )
    print( '|_________________' )
    print( '\n' )
    
    printCurrentWordState()

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

def printCurrentWordState():
    print( selectedWord )
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
def processGuess( guess ):
    global selectedWordLetters
    global blankIndicators
    global currentWordState

    matchFound = False
    
    for i in range( len(selectedWordLetters) ):
        if( blankIndicators[i] == 0 and
            currentWordState[i] == '_' ):
            if( selectedWordLetters[i] == guess ):
                matchFound = True
                currentWordState[i] = guess

    return matchFound
    
def main():
    global incorrectGuesses
    global correctGuesses
    
    print( '\n\n' )

    printBanner()
    loadDictionary()
    selectWord()
    createChallenge()
    
    while True:
        printHangman()
        prompt = '\n\n\n>> '
        guess = input(prompt)
        result = processGuess( guess[0] )
        if( result == False ):
            incorrectGuesses += 1
            print( 'Incorrect!', (6-incorrectGuesses), 'guesses left')
        else:
            print( 'Correct!' )
            correctGuesses.append(guess)

        if list(dict.fromkeys(selectedWordLetters)) == list(dict.fromkeys(correctGuesses)):
            print( 'win' )
            return

        
main();

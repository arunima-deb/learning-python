import random

# Data/Variables
words = []
selectedWord = 'Q'

numUnderscore = []
row4 = ( '|          ', '|        O' )
row4range = 1
row5 = ( '|          ', '|       /', '|       /|',
                '|       /|\\' )
row6 = ('|          ', '|       /', '|       / \\' )
incorrectGuesses = 0
guessesLeft = 6
correctLetter = 'E'
incorrectGuesses = 0
correctGuesses = []
usedLetters = []
selectedWordArray = []
for c in selectedWord:
    selectedWordArray.append(c)

selectedWordLetters = []
blankIndicators = []
currentWordState = []


# Loads a list of words from a text file. This function assumes
# that each line of the file is a word. If a line is empty or
# contains a single character, the line is ignored.
def loadDictionary():
    global words
    
    file = open( "HangmanWords.txt" )
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

printBanner()    

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

    print(selectedWordLetters)
    print(blankIndicators)
    print(currentWordState)

def printCurrentWordState():
    for index in range( 0, len(selectedWord) ):
        if blankIndicators[index] == 0:
            print( '[', currentWordState[index], ']', sep='', end=' ')
        else:
            print( currentWordState[index], end=' ')

def main():
    global guessesLeft
    global incorrectGuesses
    global correctGuesses
    global usedLetters
    global selectedWordArray
    global selectedWord

    print( '\n\n' )

    loadDictionary()
    selectWord()
    createChallenge()
    printCurrentWordState()
    
    while True:
        printHangman()
        prompt = '\n\n\n>> '
        guess = input(prompt)
        if guess in usedLetters:
            print( 'This letter was already used!' )
        if len(guess) > 1:
            print( 'Invalid' )
            return
        else:    
            for c in selectedWord:
                if c == guess:
                    correctLetter = c
                    correctGuesses.append(c)
                    print( 'Correct!' )
                    usedLetters.append(c)
                
        if guess not in selectedWord:
            guessesLeft -= 1
            incorrectGuesses += 1
            if guessesLeft > 0:
                print( 'Sorry! You have', guessesLeft, 'guesses left.' )
            else:
                print( 'Sorry! You have', guessesLeft, 'guesses left.' )
                print( 'man hanged...' )
                printHangman()
                return


main()

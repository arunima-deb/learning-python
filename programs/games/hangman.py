import random
# prompt = 'enter number : '
# x = int(input(prompt))

# print( ' _________', '\n|         |'*(int(x/2)), '\n|'*((x-(int(x/3)))-1), '________________', sep='' )

# print( '\n\n\t\t O', '\n\t\t/', '|', '/', sep='' )

words = [ 'acute', 'acme', 'acquit', 'introvert', 'extraneous', 'fabric',
          'fatal', 'falter', 'fodder', 'foreshadow' ]
selectedWord = 'E'

ranNum = int(random.randint(0, 9))
selectedWord = words[ranNum]
print( selectedWord )

for c in selectedWord:
    print( c, end=' ' )
print()
# print( '_ '*len(selectedWord) )'

numUnderscore = []

for c in range(len(selectedWord)):
    numUnderscore.append( '_ ' )
    
for c in numUnderscore:
    print( c, end=' ' )

# Print title
print( "\n  Multiplication with working\n" )

# Collect problem statement and extract the numbers
prompt = "Enter multiplication sum : "
multiplication = input(prompt)
numbers = multiplication.split( 'x' )

num1 = int(numbers[0].strip())
num2 = int(numbers[1].strip())

# Determine big and small numbers
bigNum = num1
smallNum = num2

if num2 > num1:
    bigNum = num2
    smallNum = num1

# Determine whether numbers are positive or negative
bignumSign = '-'
if bigNum > 0:
    bignumSign = ''

smallnumSign = '-'
if smallNum > 0:
    smallnumSign = ''

# Create a list for digits in the smaller number
digit_smallnum = [int(c) for c in str(smallNum)]
digit_smallnum.reverse()

# Compute indivisual working values
i = 0
valueArr = []
for digit in digit_smallnum:
    
    faceValue = digit_smallnum[i]
    placeValue= faceValue * (10**i)
    value = bigNum * placeValue
    
    valueArr.append( value )
    i += 1

# Compute final result
finalResult = bigNum*smallNum

# Convert all values into a string and store them in an array
# bigNum, smallNum, valueArr, finalResult
allArr = []
allArr.append( "  " + str(bigNum) )
allArr.append( "x " + str(smallNum).rjust( len(str(bigNum)) ) )
allArr.append( "_" + "_"*len(str(bigNum)) )

for value in valueArr:
    if value != 0:
        allArr.append( str(value) )
    
allArr.append( str(finalResult) )

# Find length of largest string in allArr
maxLen = 0
for item in allArr:
    itemLen = len(item)
    if len(str(itemLen)) > len(str(maxLen)):
        maxLen = str(itemLen)

# Printing the problem and its working
print()
print( '\t', ' '*(maxLen-len(bigNum)), bigNum )
print( '\t' )

print('\n')
if '-' not in str(bigNum):
    print( 'Answer = ', finalResult, sep='' )
    
if '-' in str(bigNum):
    print( 'Answer = ', bignumSign, finalResult, sep='' )

# 15/5/22
# the way baba has printed the working won't work for negative numbers
# change way of printing working

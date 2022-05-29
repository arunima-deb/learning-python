prompt = "Enter two number multiplication sum : "
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

digit_bignum = [int(c) for c in str(bigNum)]
    
# Create a list for digits in the smaller number
digit_smallnum = [int(c) for c in str(smallNum)]
digit_smallnum.reverse()

print()
print( '  ', bigNum, sep='' )
print( 'x ', ' '*(len(str(bigNum))-len(str(smallNum))), smallNum, sep='' )
print( '_'*(len(str(bigNum))+2) )

# Compute indivisual working values
i = 0
value_arr = []
valueArr = []
for digit in digit_smallnum:
    value = (bigNum*(digit_smallnum[i]))*(10**i)
    value_arr.append( value )

    faceValue = digit_smallnum[i]
    placeValue= faceValue * (10**i)
    value = bigNum * placeValue

    valueArr.append( value )
    i += 1

for value in value_arr:
    print( value )
# Compute final result
finalResult = bigNum*smallNum

# Convert all values into a string and store them in an array
# bigNum, smallNum, valueArr, finalResult
allArr = []
allArr.append( "  " + str(bigNum) )
allArr.append( "x " + str(smallNum).rjust( len(str(bigNum)) ) )
allArr.append( "_" + "_"*len(str(bigNum)) )

print( '_'*(len(str(bigNum))+2) )
print( bigNum*smallNum )
for value in valueArr:
    if value != 0:
        allArr.append( str(value) )

allArr.append( str(finalResult) )

# Find length of largest string in allArr
maxLen = 0
for item in allArr:
    itemLen = len(item)
    if itemLen > maxLen:
        maxLen = itemLen

# Printing the problem and its working
print()
i = 0
for item in allArr:
    print( '\t', item.rjust(maxLen) )
    i += 1
    if i == (len( allArr )-1) :
        print( '\t', '_'*maxLen )

print( allArr )        

prompt = "Enter two number multiplication sum : "
multiplication = input(prompt)
# multiplication = "45555x11111111111"
numbers = multiplication.split( 'x' )

num1 = int(numbers[0].strip())
num2 = int(numbers[1].strip())

bigNum = num1
smallNum = num2

if num2 > num1:
    bigNum = num2
    smallNum = num1

digit_bignum = [int(c) for c in str(bigNum)]
digit_smallnum = [int(c) for c in str(smallNum)]
digit_smallnum.reverse()

print()
print( '  ', bigNum, sep='' )
print( 'x ', ' '*(len(str(bigNum))-len(str(smallNum))), smallNum, sep='' )
print( '_'*(len(str(bigNum))+2) )

i = 0
value_arr = []
for digit in digit_smallnum:
    value = (bigNum*(digit_smallnum[i]))*(10**i)
    value_arr.append( value )
    i += 1

for value in value_arr:
    print( value )

print( '_'*(len(str(bigNum))+2) )
print( bigNum*smallNum )

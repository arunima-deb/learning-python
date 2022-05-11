prompt = "Enter two number multiplication sum : "
multiplication = input(prompt)
numbers = multiplication.split( 'x' )

num1 = numbers[0].strip()
num2 = numbers[1].strip()

bigNum = num1
smallNum = num2

if len(num2) > len(num1):
    bigNum = num2
    smallNum = num1

digit_bignum = [c for c in bigNum]
digit_smallnum = [c for c in smallNum]

print( bigNum*digit_smallnum[0] )
print( digit_bignum, digit_smallnum )  
print()
print( '  ', bigNum, sep='' )
print( 'x ', ' '*(len(bigNum)-len(smallNum)), smallNum, sep='' )
print( '_'*(len(bigNum)+2) )

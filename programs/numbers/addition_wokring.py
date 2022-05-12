prompt = "Enter problem : "
additionSum = input(prompt)
numbers = additionSum.split( '+' )

num1 = numbers[0].strip()
num2 = numbers[1].strip()

bigNum = num1
smallNum = num2

if len(num2) > len(num1):
    bigNum = num2
    smallNum = num1

digit_bignum = [c for c in bigNum]
digit_smallnum = [c for c in smallNum]

print( bigNum, smallNum )

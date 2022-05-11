# Five times the sum of a two digit number equals the number.
# When nine is added to the number, its digits are reversed.
# Find the number

for tensDigit in range(1,10):
    for onesDigit in range(10):
        number = tensDigit*10 + onesDigit
        reverseNumber = onesDigit*10 + tensDigit
        sumOfDigits = tensDigit + onesDigit

        if( 5*(tensDigit + onesDigit) == number ):
            if( number + 9 == reverseNumber ):
                print( "Answer =", number )
                break

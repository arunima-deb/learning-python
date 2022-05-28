promptNumerator = "Enter numerator : "
numerator = int(input(promptNumerator))

promptDenominator = "Enter denominator : "
denominator = int(input(promptDenominator))
if '0' in str(denominator):
    print( 'I', 'n', 'v', 'a', 'l', 'i', 'd', sep='' )

def printFraction( numerator, denominator ):
    print()
    print( '\t\t', numerator, sep='' )
    print( 'Fraction:   ', '   ---', sep='' )
    print( '\t\t', denominator, sep='' )
    print()

def factorize( denominator ):
   print("The factors of", denominator, "are : ")
   for i in range(1, denominator+1):
       if denominator % i == 0:
           print( (denominator/i) )



printFraction( numerator, denominator )
factorize( denominator )

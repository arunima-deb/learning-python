# Collect Numerator
promptNumerator = "Enter numerator : "
numerator = int(input(promptNumerator))

# Collect Denominator, return error if Denominator is zero
promptDenominator = "Enter denominator : "
denominator = int(input(promptDenominator))
if denominator == 0:
    print( '\nCannot divide by zero!!', sep='' )

# Prints  fraction without simplifying
def printFraction( numerator, denominator ):
    if denominator == 0:
        print( ' ' )
    else:    
        print()
        print( '\t\t', numerator, sep='' )
        print( 'Fraction:   ', '   ---', sep='' )
        print( '\t\t', denominator, sep='' )
        print()

# This function takes an integer value and returns an array of
# integers, each of which are factors of the given number
def factorize( value ):
    factors = []
    if value != 0:       
        for number in range(1, value+1):
            if value % number == 0:
                factors.append(number)
    return factors

# Finds and returns highest common factor of numerator and denominator
def findHCF( factors1, factors2 ):
    commonFactors = []
    for factor in factors1:
        if factor in factors2:
            commonFactors.append(factor)
    return max(commonFactors)

printFraction( numerator, denominator )
numeratorFactors = factorize( numerator )
denominatorFactors = factorize( denominator )

def simplify( numerator, denominator, HCF ):
    simNumerator = ( int(numerator/HCF) )
    simDenominator = ( int(denominator/HCF) )
    print( 'Simplified Fraction = ', simNumerator, '/', simDenominator, sep='' )

print( "Factors of numerator", numerator, "are", numeratorFactors )
print( "Factors of denominator", denominator, "are", denominatorFactors )

HCF = findHCF( numeratorFactors, denominatorFactors )
print( 'HCF = ', HCF )

simplify( numerator, denominator, HCF )

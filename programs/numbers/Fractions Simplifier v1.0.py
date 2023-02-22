# Title
print( '\n\tFractions Simplifier v. 1.0\n' )

simNumerator = 'e'
simDenominator = 'f'
integralPart = 'g'

# Collect Numerator
promptNumerator = "Enter numerator : "
numerator = int(input(promptNumerator))


# Collect Denominator, return error if Denominator is zero
promptDenominator = "Enter denominator : "
denominator = int(input(promptDenominator))
if denominator == 0:
    print( '\nCannot divide by zero!!', sep='' )


# Prints fraction without simplifying
def printOriginalFraction( numerator, denominator ):
    if denominator == 0:
        print( ' ' )
    else:    
        print( '\nOriginal Fraction = ', numerator, '/', denominator, sep='' )


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

def simplify( numerator, denominator ):
    integralPart = 0
    simNumerator = numerator
    simDenominator = denominator
    
    if simNumerator > simDenominator:
        integralPart = int(simNumerator/simDenominator)
        simNumerator = simNumerator - (simDenominator*integralPart)

    numeratorFactors = factorize( simNumerator )
    denominatorFactors = factorize( simDenominator )
    HCF = findHCF( numeratorFactors, denominatorFactors )

    simNumerator = int(simNumerator/HCF)
    simDenominator = int(simDenominator/HCF)

    if integralPart != 0:
        print( '\nSimplified Fraction = ', integralPart, ' ', simNumerator, '/', simDenominator, sep='' )
    else:
        print( '\nSimplified Fraction = ', simNumerator, '/', simDenominator, sep='' )


printOriginalFraction( numerator, denominator )
simplify( numerator, denominator )


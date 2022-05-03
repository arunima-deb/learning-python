# Program to print the expanded form of a given number
# The program continues till the user enters 'exit'
# at the prompt.

str = input( "Enter a number or 'exit' to quit: " )

while str != 'exit':
    
    print( "Number entered is :", str )

    if( not str.isdigit() ):
        print( "\tNumber is not an integer" )
    else:
        length = len(str)
        for i in range( length ):
            ending = '+' if (i < length-1) else ''
            print( str[i], 'x', 10**(length - i - 1), ending )

    str = input( "\nEnter a number or 'exit' to quit: " )


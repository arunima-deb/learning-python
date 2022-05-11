# Program to test if the entered number is even or odd
# The program continues till the user enters 'exit'
# at the prompt.

str = input( "Enter a number or 'exit' to quit: " )

while str != 'exit':
    
    print( "Number entered is :", str )

    num = int( str )

    if( num % 2 == 0 ):
        print( "\tNumber is even" )
    else:
        print( "\tNumber is odd" )

    str = input( "\nEnter a number or 'exit' to quit: " )


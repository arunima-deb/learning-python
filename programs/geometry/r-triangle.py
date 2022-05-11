print( "\n   Right Triangle\n" )
prompt = "Enter height of triangle : "
<<<<<<< HEAD
side = int(input(prompt))
print()

for r in range(side):
    starting_spaces = side-(r+1)
    num_dot = r+1
    print( '  '*starting_spaces, ' .'*num_dot, sep='' )
=======
# side = int(input(prompt))
side = 7

for r in range(side):
    num_starting_spaces = 0
    num_X = r+1
    num_ending_spaces = side - (r+1)
    print( ' '*num_starting_spaces, ' X'*num_X, ' '*num_ending_spaces, sep='' )

    
>>>>>>> e53a807009375d586d211cfbf019c6c9e9370665

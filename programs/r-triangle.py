prompt = "Enter height of triangle : "
# side = int(input(prompt))
side = 7

for r in range(side):
    num_starting_spaces = 0
    num_X = r+1
    num_ending_spaces = side - (r+1)
    print( ' '*num_starting_spaces, ' X'*num_X, ' '*num_ending_spaces, sep='' )

    

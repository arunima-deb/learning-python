print( "\n   Right Triangle\n" )
prompt = "Enter height of triangle : "
side = int(input(prompt))
print()

for r in range(side):
    starting_spaces = side-(r+1)
    num_dot = r+1
    print( '  '*starting_spaces, ' .'*num_dot, sep='' )

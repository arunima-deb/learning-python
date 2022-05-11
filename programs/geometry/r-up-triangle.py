print( "\n   Right Up Triangle\n" )
prompt = "Enter height of triangle : "
side = int(input(prompt))
print()

for r in range(side):
    StartingSpaces = r
    NumDot = side - 1
    EndingSpaces = 0
    print( '  '*StartingSpaces, ' .'*NumDot, ' '*EndingSpaces, sep='' )
    side = side - 1

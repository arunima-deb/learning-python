print( "\n   Left Up Triangle\n" )
prompt = "Enter side of triangle : "
side = int(input(prompt))
print()

for r in range(side):
    NumDot = side - 1
    EndingSpaces = side - side
    print( ' .'*NumDot, ' '*EndingSpaces, sep = '' )
    side = side - 1

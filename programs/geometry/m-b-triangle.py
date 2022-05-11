prompt = "Enter height of triangle : "
h = int(input(prompt))
print()

for r in range(h):
    startingSpaces = r
    numDot = h - r
    print( ' '*startingSpaces, '. '*numDot, sep='' )

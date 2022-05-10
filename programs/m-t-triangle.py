prompt = "Enter height of triangle : "
h = int(input(prompt))
print()

for r in range(h):
    startingSpaces = h - r - 1
    numDot = r + 1
    print( ' '*startingSpaces, '. '*numDot, sep='' )

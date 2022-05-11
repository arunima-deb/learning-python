print( "\n", " "*3, "Middle Triangle\n" )
prompt = "Enter base of triangle : "
base = int(input(prompt))

for r in range(base):
    StartingSpaces = int(base/2)
    NumDot = int(base/(base-r))
    EndingSpaces = int(base/2)
    base = base - 1
    print( ' '*StartingSpaces, ' .'*NumDot, ' '*EndingSpaces, sep='' )

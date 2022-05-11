prompt = "Enter size of arrow head : "
side = int(input(prompt))
num = side - 1

for r in range(side):
    StartingSpaces = 0
    EndingSpaces = 0
    NumDot = int(side/2)
    print( ' '*StartingSpaces, ' .'*NumDot, ' '*EndingSpaces, sep='' )

    

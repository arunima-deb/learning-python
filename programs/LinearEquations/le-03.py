x = 0
lhs = 5*x - 17
rhs = 2*x - 8

solutionFound = (lhs == rhs)

while not solutionFound:
    x=x+1
    lhs = 5*x - 17
    rhs = 2*x - 8

    solutionFound = (lhs == rhs)

print( "Solution =", x )

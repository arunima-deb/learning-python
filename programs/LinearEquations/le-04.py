# Collect equation
prompt1 = "Enter equation : "
equation = input(prompt1)

# split equation into LHS and RHS
parts = equation.split( '=' )

lhExpr = parts[0]
rhExpr = parts[1]

x = 0
lhs = eval( lhExpr )
rhs = eval( rhExpr )

solutionFound = (lhs == rhs)

while not solutionFound:
    x=x+1

    lhs = eval( lhExpr )
    rhs = eval( rhExpr )

    solutionFound = (lhs == rhs)

print( "Solution x =", x )

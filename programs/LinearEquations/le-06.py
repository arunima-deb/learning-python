# Collect equation
prompt1 = "Enter equation : "
equation = input( prompt1 )

# split equation into LHS and RHS
parts = equation.split( '=' )

lhExpr = parts[ 0 ].strip()
rhExpr = parts[ 1 ].strip()

def dist(x):
    return abs(eval(lhExpr) - eval(rhExpr))

x = 0
solutionFound = False
step = 1

dist0 = dist(0)
dist1 = dist(1)

if dist0==0:
    solutionFound = True
else:
    if dist0 < dist1:
        step=-1

while not solutionFound:
    x += step
    if dist(x)==0:
        solutionFound = True

print( "Solution x =", x )

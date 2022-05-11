# Collect equation
prompt1 = "Enter equation : "
equation = input( prompt1 )

# split equation into LHS and RHS
parts = equation.split( '=' )

lhExpr = parts[ 0 ].strip()
rhExpr = parts[ 1 ].strip()

def dist(x):
    return eval(lhExpr) - eval(rhExpr)

def sign(distance):
    if distance < 0:
        return -1
    elif distance > 0:
        return 1
    return 0

x = 0
solutionFound = False
step = 0.01
lastSign = 0 ;

dist0 = dist(0)
dist1 = dist(1)

if dist0==0:
    solutionFound = True
else:
    lastSign = sign( dist0 )
    if abs(dist0) < abs(dist1):
        step=-0.01

while not solutionFound:
    x += step
    currentDistance = dist(x)
    currentSign = sign( currentDistance )

    if currentDistance == 0:
        solutionFound = True
        break
    elif currentSign != lastSign:
        solutionFound = True
        x -= step/2
        break
    else:
        lastSign = currentSign

print( "Solution x =", round(x,2) )

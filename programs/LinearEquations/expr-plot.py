# Takes a linear equation and plots LHS and RHS as two
# line graphs using matplotlib

import matplotlib.pyplot as plt

expr = "x=2"
parts = expr.split( '=' )
lhExpr = parts[0].strip()
rhExpr = parts[1].strip()

lhYVals = []
rhYVals = []
xVals   = []

for x in range(-20,20):
    xVals.append( str(x) )
    lhYVals.append( eval( lhExpr ) )
    rhYVals.append( eval( rhExpr ) )

plt.plot( xVals, lhYVals )
plt.plot( xVals, rhYVals )
plt.grid()
plt.legend( [lhExpr, rhExpr] )
plt.show()

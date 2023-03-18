uValues = [ 80, 90, 100, 91, 86, 83, 87, 94.2, 87.2 ]
vValues = [ 65.9, 64.2, 63.3, 64.2, 64.8, 65.5, 64.8, 64, 64.6 ]
sumOfAllF = 0


for i in range(len(uValues)):
    u = uValues[i] - 50
    v = vValues[i] - 50
    f = (u*v)/(u+v)
    sumOfAllF += f

print( "Focus =", sumOfAllF/len(uValues) )

##uReciprocal = []
##vReciprocal = []
##fValues = []
##
##for val in u:
##    uReciprocal.append( 1/val )
##
##for val in v:
##    vReciprocal.append( 1/val )
##
##for i in range( len(u) ):
##    fValues.append( 1/(uReciprocal[i] + vReciprocal[i]) )
##    
##for val in fValues:
##    print( val )

# Data/Variables
global elements
global atomicMasses
global evenNum
global allTermsinFile
global atomicNum

elements = []
atomicMasses = []
evenNum = 0
allTermsinFile = []
atomicNum = int(input("Enter atomic number : "))

# Collects RAM of elements 1-30
def getAtomicMass():
    for i in range(1, 21):
        if i == 1:
            atomicMasses.append(int(1))
        elif i == 4:
            atomicMasses.append(int(9))
        elif i == 7:
            atomicMasses.append(int(14))
        elif i == 18:
            atomicMasses.append(int(40))
        else:
            if i%2 == 0:
                atomicMasses.append(int(2*i))
            else:
                atomicMasses.append(int(2*i+1))

# Prints Mass number of an element taking it's atomic number as input
def printAtomicMass( atomicNum ):
    print( "Atomic mass of the ", atomicNum, "th element = ", atomicMasses[atomicNum-1], sep = '' )
    print( "\n" )
    
getAtomicMass()
printAtomicMass( atomicNum )

# Title
print( '\n   Simple Calculator v. 1.0\n' )

# Collect problem
prompt = 'Enter sum : '
problem = str(input(prompt))

def determineOperation( problem ):
    operation = 'E'
    
    if '+' in problem:
        addition = problem.split( '+' )
        operation = '+'
        print(addition)
        
    if '-' in problem:
        subtraction = problem.split( '-' )
        operation = '-'
        
    if 'x' in problem:
        multiplication = problem.split( 'x' )
        operation = 'x'

    if '/' in problem:
        division = problem.split( '/' )
        operation = '/'

    return operation
    return addition
        
def addition(addition, operation):
    print( (addition(0)) + (addition(1)) )
    

determineOperation( problem )        
addition(addition, operation)

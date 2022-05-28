# Title
print( '\n   Simple Calculator v. 1.0\n' )

# Collect problem
prompt = 'Enter sum : '
problem = str(input(prompt))

def determineOperation( problem ):   
    if '+' in problem:
        print(problem.split( '+' ))
    if '-' in problem:
        print(problem.split( '-' ))
    if 'x' in problem:
        print(problem.split( 'x' ))

        
determineOperation( problem )        

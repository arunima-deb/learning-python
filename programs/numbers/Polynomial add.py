# Title
print( '\n    Polynomial addition\n' )

# Collects sum
prompt = "Enter sum : "
problem = input(prompt)

terms = problem.split( ' + ' )

for term in terms:
    if '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in term:
        term.strip( '0123456789' )
        

print(terms)

________
|       |
|       |
|       O
|      /|\
|      / \
|____________

 h _ _ g _ a _      

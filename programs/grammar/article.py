prompt = 'Enter who you want to be : '
ambition = input( prompt )

while ambition != 'exit':
    article = 'a'
    f = ambition[0].lower()
    if( "aeiou".find( f ) != -1 ):
        article = 'an'

    print( "  →I want to be ", article, " ", ambition, ".", sep="" )
        
    ambition = input( "\n" + prompt )

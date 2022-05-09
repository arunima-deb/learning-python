prompt = "Enter height of triangle : "
# h = int(input(prompt))
h = 7
one = 1
for row in range(h):
    if( row == 0 ):
        print( "  "*h, ".", "  ", sep='' )
    else:
        print( ("  "*(h-1), ".", " ."*(one+1)), sep='' )
        h = h-1
        
        

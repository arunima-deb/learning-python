prompt = "Enter height of triangle : "
side = int(input( prompt ))
print( '' )

row = 1
while row <= side:
    print( '. '*row, end=' ' )
    print( '' )
    row = row+1

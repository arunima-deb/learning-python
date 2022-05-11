prompt = "Enter length of square side : "
side = int(input( prompt ))
print( '' )

row = 0
while row < side:
    col = 0
    while col < side:
        print( '.', end=' ' )
        col = col+1
    print( '' )
    row = row+1

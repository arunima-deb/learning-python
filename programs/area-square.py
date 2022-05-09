# collect side of square
prompt1 = "Enter side of square : "
side = int(input(prompt1))

# collect unit of measurement
prompt2 = "Enter unit of measurement : "
unit = input(prompt2)
print( '' )

# compute area = side x side
area = side*side

# compute perimeter = 4 x side
perimeter = 4*side

# print area
print( "Area = ", area, " sq.", unit, sep='' )

# print perimeter
print( "Perimeter = ", perimeter, " ", unit, sep='' )

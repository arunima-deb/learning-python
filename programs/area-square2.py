# collect side of square
prompt1 = "Enter side of square (Kindly leave a space between length of side and unit of measurement.) : "
input_str = input(prompt1)
print( '' )

# split input into unit of measurement and length
parts = input_str.split()

# First part is the length of side. Convert it into int. Assign it to a variable called side
length_side = int(parts[0])

# Second part is unit of measurement. Assign it to a variable unit
unit_measurement = parts[1]

# compute area = side x side
area = length_side*length_side

# compute perimeter = 4 x side
perimeter = 4*length_side

# print area
print( "Area = ", area, " sq.", unit_measurement, sep='' )

# print perimeter
print( "Perimeter = ", perimeter, " ", unit_measurement, sep='' )

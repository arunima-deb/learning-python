import time
for x in range(2):
    time.sleep(1)
    print("\t\r X | O | O ".format(x), end="")
    print()
    time.sleep(1)
    print("\t\r---+---+---".format(x), end="")
    print()

print("\t X | O | O ")    



print('\n')
print('\t      a   b   c')
print()
for x in range(2):
    time.sleep(0.25)
    print("\t", y, '\r     |', a1, '|   ', end="")
    print()
    time.sleep(0.25)
    print("\t\r     ---+---+---", end="")
    print()
    y = y+1

print("\t", '3  ', "   |", a3, "|   ")
print('\n')

prompt = "Enter where you want to place X : "
placetilehere = input(prompt)

if placetilehere := a1:
    a1 = 'x'
    for x in range(2):
        time.sleep(0.25)
        print("\t", y, '\r     |', a1, '|   ', end="")
        print()
        time.sleep(0.25)
        print("\t\r     ---+---+---", end="")
        print("\t", '3  ', "   |", a3, "|   ")
        print('\n')
        y = y+1


if place_x_here := a2:
    a2 = '[X]'
    print_board()
 
if place_x_here := a3:
    a3 = '[X]'
    print_board()
 
if place_x_here := b1:
    b1 = '[X]'
    print_board()
 
if place_x_here := b2:
    b2 = '[X]'
    print_board()
 
if place_x_here := b3:
    b3 = '[X]'
    print_board()
 
if place_x_here := c1:
    c1 = '[X]'
    print_board()
 
if place_x_here := c2:
    c2 = '[X]'
    print_board()
 
if place_x_here := c3:
    c3 = '[X]'
    print_board()        
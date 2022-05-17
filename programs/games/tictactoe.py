import time

row = [ ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ]
sep = [ '-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-', ]
y = 1

a1 = 'o'
b1 = 'x'
c1 = 'x'
a2 = 'x'
b2 = 'x'
c2 = 'x'
a3 = 'x'
b3 = 'x'
c3 = 'x'

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
        y = y+1

    

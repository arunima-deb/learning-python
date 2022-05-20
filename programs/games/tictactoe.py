import time

a1 = '[ ]'
b1 = '[ ]'
c1 = '[ ]'
a2 = '[ ]'
b2 = '[ ]'
c2 = '[ ]'
a3 = '[ ]'
b3 = '[ ]'
c3 = '[ ]'


def print_board():
    print('\n')
    print('\t      a   b   c')
    print()
    y = 1
    print("\t", y, ' ', a1, b1, c1 )
    print()
    y = y+1
    print("\t", y, ' ', a2, b2, c2 )
    print()
    y = y+1
    print("\t", y, ' ', a3, b3, c3 )
    print()
    y = y+1
    prompt = "Enter where you want to place X : "
    place_x_here = input(prompt)

    
def check_win():
    if a1 == '[X]':
        if b2 == '[X]':
            if c3 == '[X]':
                print( 'X wins!' )
                
print_board()

if 'a1' in str(place_x_here):
    a1 = '[X]'
    print_board()
    
if 'a1' not in str(place_x_here):
    if 'a2' in str(place_x_here):
        a2 = '[X]'
        print_board()

if 'a1' not in str(place_x_here):
    if 'a3' in str(place_x_here):
        a3 = '[X]'
        print_board()

if 'a1' not in str(place_x_here):
    if 'b1' in str(place_x_here):
        b1 = '[X]'
        print_board()

if 'a1' not in str(place_x_here):
    if 'b2' in str(place_x_here):
        b2 = '[X]'
        print_board()

if 'a1' not in str(place_x_here):
    if 'b3' in str(place_x_here):
        b3 = '[X]'
        print_board()

        

def printTitle():
    print( "  ___        _           _                   _   __  " )
    print( " | __|_ _ __| |_ ___ _ _(_)___ ___ _ _  __ _/ | /  \ " )
    print( " | _/ _` / _|  _/ _ \ '_| (_-</ -_) '_| \ V / || () | ")
    print( " |_|\__,_\__|\__\___/_| |_/__/\___|_|    \_/|_(_)__/  " )
    print( "\n\n")

def collectNum():
    prompt = "Enter integer : "
    num = int(input(prompt))
    print(num)

printTitle()
collectNum()

def primeFactorise():
    for naturalNum in range(9):
        

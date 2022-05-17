import time
for x in range(2):
    time.sleep(1)
    print("\t\r X | O | O ".format(x), end="")
    print()
    time.sleep(1)
    print("\t\r---+---+---".format(x), end="")
    print()

print("\t X | O | O ")    


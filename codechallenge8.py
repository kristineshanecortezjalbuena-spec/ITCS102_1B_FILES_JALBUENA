rows = 7
for x in range(rows):
    for y in range(rows):
        if x+y == 3:
            print("*", end=" ")
        elif x+y == 5 and y != 5 and x != 5:
            print("*", end=" ")
        elif x+y == 7 and y != 6 and x != 6:
            print("*", end=" ")
        elif x+y == 9:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()       

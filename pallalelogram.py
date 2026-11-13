rows = 7
for x in range(rows):
    for y in range(rows):
        if x + y == 3 or x + y == 7 and x != 6 and y != 6:
            print("*", end=" ")
        elif x == y - 3 and y != 6 or y == x - 3 and x != 6: 
            print("*", end=" ")    
        else:
            print(" ", end=" ")
    print()           

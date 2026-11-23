bini = []

isContinuing = True

while isContinuing:
    ans = input("Do you want to add a title of an bini (y/n): ") == "y"
    if ans == True:
        title = input("Enter the title of an bini:  ")
        bini.append(title)
        print(bini)
        
    else:
        isContinuing = False
        print(bini)
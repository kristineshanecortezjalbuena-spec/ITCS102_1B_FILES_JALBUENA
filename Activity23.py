
#summation program

num = int(input("Enter a number -> "))


def my_factorial(sagot):
    fact = 1
    for x in range(sagot, 0, -1):
        fact *= x
    return fact
    
def sh_eyn(name):
    bati = "hi" + name
    return bati
    
print("output", my_factorial(13))
print("output", my_factorial(7))
print("output", my_factorial(8))
print("output", my_factorial(5))
print("output", my_factorial(21))

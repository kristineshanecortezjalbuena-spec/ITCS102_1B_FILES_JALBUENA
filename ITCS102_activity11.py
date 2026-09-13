#import demo
import getpass

username = "loveu"
password = "loveusm"

u = input("Input USERNAME ---> ")
p = getpass.getpass("Input PASSWORD ---> ")

if u == username and p == password:
    print ("username and password correct")
else:
    print("access denied")
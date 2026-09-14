# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int(input("Enter age --> "))
is_employed = bool(input("Are you current employed --> "))
credit_score = eval(input("Credit Score history --> "))
annual_income = eval(input("How much is your annual income --> "))
has_collateral = bool(input("Do you have collateral --> "))

if age >= 21 and is_employed == True:
    print("pwede, boss")
else:
    print("Di pede boss, sorry.")
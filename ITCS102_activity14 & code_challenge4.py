# LOGIN
username = input("Enter username: ")
password = input("Enter password: ")

# Example login credentials
if username == "bdo123" and password == "1229":

    # COLLATERAL
    collateral = input("Enter collateral (motorcycle, land, house, etc.): ")
    collateral_value = float(input("Enter collateral value: "))

    if collateral_value < 30000:
        print("Invalid: Collateral value must be at least 30k")

    else:
        age = int(input("Enter age: "))
        employed = input("Currently employed? (True/False): ")

        credit_score = int(input("Enter credit score: "))
        annual_income = float(input("Enter annual income: "))

        employed = employed == "True"

        if age < 21 or not employed:
            print("Rejected: Fails baseline criteria")

        else:

            if credit_score >= 750:
                interest_rate = 5.0

                if annual_income >= 100000:
                    interest_rate = 4.5

                print("Approved")
                print("Credit Tier: High Credit")
                print("Interest Rate:", interest_rate, "%")

            elif credit_score >= 600:
                interest_rate = 8.0

                if collateral_value >= 30000:
                    interest_rate = 7.0

                elif annual_income < 40000:
                    interest_rate = 9.5

                print("Approved")
                print("Credit Tier: Fair Credit")
                print("Interest Rate:", interest_rate, "%")

            else:
                print("Rejected: Credit score too low")

else:
    print("Login failed: Invalid username or password")
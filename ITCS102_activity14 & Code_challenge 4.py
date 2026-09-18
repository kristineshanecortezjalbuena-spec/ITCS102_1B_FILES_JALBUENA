
# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolea)

need login
usernmae, password

prompt user to enter name/description of collateral e.g motorcyle, land, house,
promt user the value of the collateral anything less than 30k is invalid

maximum age for loan is 65
ask user amount to loan , and the calculated interest rate using base rate


age = int(input("Input age	"))
is_employed = bool(input("Are you currently employed (True/False)		"))
credit_score = int(input("Credit Score	"))
annual_income = float(input("Waht is your annual income	"))
has_collateral = bool(input("Do you have any collateral(True/False)	"))

employed = employed == "True"
has_collateral = has_collateral == "True"

if age < 21 or not employed:
	print("Declined, not eligible.")
	
else:
	if credit_score >= 750:
		interest_rate = 5.0
		
	if annual_income >= 100000:
		interest_rate = 4.5
		
	print("Approved")
	print("Credit Score: High Credit")
	print("Interest Rate:", interest_rate, "%")
	
elif credit_score >=600:
	interest_rate = 9.5
	
print("Approve")
print("Credit Score: Fair Credit")
print("Interest Rate:", interest_rate, "%")

else:
	print("Rejected: not eligible")

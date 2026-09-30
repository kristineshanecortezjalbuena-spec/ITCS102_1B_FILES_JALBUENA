age = int(input("Enter age  "))
rev = float(input("Enter monthly revenue    "))
cc = int(input("Enter credit score  "))
yrs_b = float(input("Years in Business    "))
has_defaults = bool(input("Default History  "))
collateral = input("Collateral Name ")
c_value = float(input("collateral value     "))

max_limit = 0
base_fee = 0.0
#baseline

if age >= 21 and yrs_b >=2 and has_defaults == False:
    print("Baseline requirments pass  ")
    
    if cc >= 720: #tier1
        max_loan = rev * 3
        print("max loan for high credfit iis ",max_loan)
        print("High Credit Score of 720")
        #monthly revenue conditions
        if rev >= 50000:
            base_fee = max_loan * 0.015
            print("base fee rate is ",base_fee)
        else:
           base_fee = max_loan * 0.025
           print("base fee is ",base_fee)
        #collateral
        if c_value >= max_loan:
            print("Collateral ", collateral, "--Acccepted")
        else:
            print("Collateral not accepted")

        #surcharge
        surcharge = max_loan * base_fee
        if c_value % 5000 != 0:
            surcharge += 250



    elif cc <=620 and cc < 720: #tier2
        max_loan = rev * 1.5
        print("max loan is set to ",max_loan)
        if yrs_b >= 5:
            base_fee = max_loan * 0.02
            print("base fee rate is ", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("base fee rate is ",base_fee)

        if c_value >= max_loan:
            print("Collateral", collateral, "--Accepted")
        else:
            print("Collateral not accepted")
    elif cc < 620:
        print("Credit score too low for a loan")
    else:
        print("Not tier 1")
else:
    print("Rejected: High Risk Application or Ineligible Owner")
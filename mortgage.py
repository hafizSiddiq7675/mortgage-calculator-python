# Three things that use will provide
# 1) Principal Amount
principal_amount = 0
# 2) Interest Rate Monthly.(Annual rate divided by 12)
interest_rate_monthly = 0
# 3) Total number of payments. (Number of years multiplyed by 12)
number_of_payments = 0
# taking input from user 
# Get the loan amount
principal_amount = int(input("Enter Principal Amount: "))
# Get the interest rate Monthly
interest_rate_monthly = float(input("Enter interest Rate: "))
interest_rate_monthly = interest_rate_monthly / 100
interest_rate_monthly = interest_rate_monthly / 12
# Get the number of years
number_of_payments = (int(input("Number of years for Mortgage payment: "))) * 12
# using formula M = P[i(1+i)^n]/[(1+i)^n-1] 
result = principal_amount * (interest_rate_monthly * (1 + interest_rate_monthly ** number_of_payments) / (((1 + interest_rate_monthly) ** number_of_payments) - 1))  
print("Your Monthly Payment will be: ")
print(result)  
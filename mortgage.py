# Three things that use will provide
# 1) Principal Amount
pAmount = 0
# 2) Interest Rate Monthly.(Annual rate divided by 12)
iRateM = 0
# 3) Total number of payments. (Number of years multiplyed by 12)
number_of_payments = 0
# taking input from user 
# Get the loan amount
pAmount = int(input("Enter Principal Amount: "))
# Get the interest rate Monthly
iRateM = float(input("Enter interest Rate: "))
iRateM = iRateM / 100
iRateM = iRateM / 12
# Get the number of years
number_of_payments = (int(input("Number of years for Mortgage payment: "))) * 12
# using formula M = P[i(1+i)^n]/[(1+i)^n-1] 
result = pAmount * (iRateM * (1 + iRateM ** number_of_payments) / (((1 + iRateM) ** number_of_payments) - 1))  
print("Your Monthly Payment will be: ")
print(result)  
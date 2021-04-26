#Given debt and a fixed repayment, how much will you have left after a period of time

balance = 438
annualInterestRate = 0.18
monthlyPaymentRate = 0.05


year = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

for month in year:
    minMonthlyPayment = monthlyPaymentRate * balance
    unpaidbal = balance - minMonthlyPayment
    newbalance = unpaidbal + (annualInterestRate / 12.0) * unpaidbal
    balance = newbalance


print("Remaining Balance: " + str((round(newbalance,2)))) # rounding it to 2 digits for the cents 

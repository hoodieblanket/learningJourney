balance = 250000 # balance of loan or debt
annualInterestRate = 0.045 # annual interest rate

initialBalance = balance
lowerBound = balance / 12 # setting lowerbound of possible solutions
compoundedInterestRate = (((annualInterestRate / 12) + 1) ** 12) # annual interest rate compounded monthly.
upperBound = (balance * (compoundedInterestRate)) / 12 # upperbound of possible solutions.
year = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

while balance > 1:
    guess = (upperBound + lowerBound) / 2 # our guess for initial payment
    for month in year:
        balance = (balance - guess)
        balance = balance + (balance * (annualInterestRate / 12))
        if balance > 0 and balance < 0.01: # balance will never truely == 0 so we need to go to closes cent 0.01
            print("Lowest Payment: " + str(round(guess,2)))
    if balance > 0.01:
        lowerBound = guess
        guess = (upperBound + lowerBound) / 2
        balance = initialBalance
    elif balance < 0:
        upperBound = guess
        guess = (upperBound + lowerBound) / 2
        balance = initialBalance



print(guess)
print(balance)

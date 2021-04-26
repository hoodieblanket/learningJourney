# Given a Credit card debt, what repayment is needed to reach a 0 balance in 12 months (nearest to 10 integer)
balance = 9878
annualInterestRate = 0.20

initialBalance = balance
payment = round((balance / 12),-1)
year = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

while balance >= 1:
    for month in year:
        balance = balance - payment
        balance = balance + (balance * (annualInterestRate / 12))
    if balance <= 0:
         print("Lowest Payment: " + str(payment))
    else:
        payment += 10
        balance = initialBalance
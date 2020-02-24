#Converting integers to binary

num = input('what number to convert to binary?\n')

if num < 0:
    isNeg = True
    num = abs(num) # convert negative into positive integer
else:
    isNeg = False
Result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result

print(result)


x = 3
answer = 0
iterationsleft = x #we are assigning the iterations we want to run through as a separate variable so that we can make changes in the loop to this variable without affecting **x**
print(answer)
while (iterationsleft != 0):
    answer = answer + x
    iterationsleft = iterationsleft - 1
print (str(x) + '*' + str(x) + ' = ' + str(answer))


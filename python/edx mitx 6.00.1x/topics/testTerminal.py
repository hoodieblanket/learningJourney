testList = [-1, -2, -3, -4]
def apply(testList,function):
    for i in range(len(testList)):
        testList[i] = function(testList[i])
        print(testList)
def power(a):
    return a ** 2

apply(testList, power)
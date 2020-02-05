def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.

    quadratic equation a * x^2 + b * x + c
    '''
    e = a*x**2
    f = b*x
    return e + f + c

# a = 3
# b = 7
# c = 25
# x = 5
# calling the function
evalQuadratic(3,7,25,5)

#Introducing Functions


`def` used to define a function
followed by `name` of function
and followed by a name i or a name for the `parameter or argument`
using the `""" docstring"""` to show the specifications explaining what the input and output is.
```python
def is_even(i):
    """
    input: i, a positive int
    Returns True if i is even, otherwise False"""
    print("hi")
    return i%2 == 0
```
`return` is a keyword that tells me that I am ready to stop the computation and whatever the following expression is,\
that is the value I will give back to the person who asked for it.


#Docstrings


Docstrings are a special type of comment that is used to document what your function is doing. It is highly recommended\
to start learning early to document all your functions: What is the input and what is the output.

In the above example, the `"""docstring"""` explains the input and output.


#Calling Functions and Scope


For example:
```python
def f(x):
    x = x + 1
    print('in f(x): x - ', x)
    return x
x = 3
z = f( x )
```
When following the code, it shows that we are creating a function `f(x)` and have not assigned a value to it. It \
represents the box we call `x`. After then function we assign `x = 3` and `z = f( x )`.

So on a global scope we assigned `x` to the value of `3` and when we run the function, it will `x = x +1 (4)` and then\
print the value of the x within the function (4). then return x.

x remains as 3 in the global scope however `z` is assigned the value of the `x` inside the function using `z = f(x)`

So F ( x ) is 4 and x (in the global scope) is 3.


####Calling a function just without parenthesis won't evaluate. 
Simply calling `f` will not produce anything however\
`f()` will evaluate to the function.


#Global vs Local Scope
Be careful with global versus local scope as the former is an assignment to a variable that will be returned on a\
global scale when called and local scope allows you to assign a variable the evaluation from your function but without\
it affecting the rest of your code due to being limited in scope.
```python
a = 10
def f(x):
    return x + a
a = 3
f(1)
```
The above will assign `a = 10` on a global scale, we define f(x) but dont evaluate yet, we proceed past the body to\
`a = 3` and this **reassigns** `a` from `10 to 3` and then we call to evaluate `f(1)`. This takes the global scope `a`\
and returns `(1) + a` which evaluates to `4`


#Defining A Function Within A Function

You can evaluate a function within a function which is referred to as a Helper Function.
```python
x = 12
def g(x):
  x = x + 1
  def h(y):
      return x + y
  return h(6)
g(x)
```

The above code assigns the global variable `x = 12` then defines `g(x)` as some code that we don't know about yet\ 
so we move onto the next line `g(x)` calling on the function. Now we proceed to assign the `local scope 13 = 12 +1`\
then we define `h(y)` as some code. Finally we `return h(6)` which calls upon the `def h(y)` function to be evaluated.\

This returns `13{x} + 6{y}` and then returns the value to the caller of `g(x)`. So even though we established a \
function for `g(x)` and called upon it; the Helper Function `returned` the value from the internal function to the\
caller.

#Return vs. Print
| Return        | Print|
|:--------------|:-----------|
|- return only has meaning inside a function|- Print can be used outside functions|
|- only one return executed inside a function|- Can execute many print statements inside a function|
|- code inside function but after return statement not executed|- code inside function can be executed after print|
|- has a value associated with it, given to function caller|- has a value associated with it, outputted to the console|

#Recursion
Inside the function, it calls itself. It breaks up the problems into pieces that I can use to reduce the problem\
down to its solution.
As long as it is not an infinite loop then I can solve the problem by reducing it into pieces until I find a solution

For example the following recursion will take a simple process of finding a base variable and multiplying the base b\
by itself for x amount of iterations.
```python
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Otherwise, exp must be > 0, so return 
    #  base* base^(exp-1). This is the recursive case.
    return base * recurPower(base, exp - 1)

recurPower(2.54,3)
```
So this is saying that we want to break it down into smaller steps to find out what 2.54^3 is equal to. Or alternately\
what 2.54 is if we multiply it by 2.54 exactly 3 times.

So while the exponent is greater than 0, then it will run a function within a function to break it down with each
exponent. thne return the base times it. We covered for the fact that if exp = 0 then as per mathematical logic, the\
base needs to evaluate 2.54^0 which will return 1.

#Iterative finding the Greatest Common Divisor GCD
```python
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
```

This code will take two inputs and find out what is the largest common integer that both inputs are divided by.\
It finds the smallest of the two values and assigns it inside a variable.

Then we keep looping until that variable divides both a & b evenly.

#Combination of a Bisection Search and a Recursive solution
If for example we needed to find a value or a letter in a string of letters and we want to do it in a way whereby\
we halve the string and ask "is it in the upper half or lower half" and continue that question until we find it:\
How could we code it to find the letter using a function, bisectional searching and recursion.

```python
def isIn(char,aStr):
    '''
    char: a letter
    aStr: a string of letters
    '''
    #in order to make sure we place the string in alphabetical order we can use the following:
    aStr = ''.join(sorted(aStr))
    #we want to assign the value from the bisectional search to a variable so we can test cases. i.e the below
    #will produce the middle of the string of letters, i.e "n" and then ask if n == char or else do code
    m = aStr[len(aStr) // 2]
    # for recursion, what is the base case or smallest case that is likely to happen
    if n == '':
        return False
    # to capture if the string is None ''
    if n == char:
        return True
    elif aStr == '' or aStr == len(1):
        return False
    else:
        if char < m:
            return isIn(char,aStr[:len(aStr) // 2])
        elif char > m:
            return isIn(char,aStr[len(aStr) // 2:])
    
    isIn("r", "abcdefghijklmnopqrstuvwxyz")
```

#Using Iterative and Bisection Search to find the exact payments required for repaying debt

Using bisectional searching and iterating through a length of time, we can divide and find an exact payment amount\
required to reach a 0 balance on the debt. This figure includes covering for interest repayments as it accrues\
interest on a monthly basis.
```python
balance = 172168 # balance of loan or debt
annualInterestRate = 0.21 # annual interest rate

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

```
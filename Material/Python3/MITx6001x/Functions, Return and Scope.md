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


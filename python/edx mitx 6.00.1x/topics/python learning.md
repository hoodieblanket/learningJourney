# Python Learning

This is not an indepth look into each topic but rather just reminders or bits of info to cover my gaps in knowledge

## IF Statements

```python
if true then proceed to this code
elif Else this code
elif Else this code
else If nothing Else then proceed to this code
```

## AND, OR, NOT

```python
and: used for boolean tests where you have two outcomes and determining if they are True or False statements to reach an 'overall' True or False
or: testing between two Truth statements and if EITHER of them are True then the overall test is that atleast one is True
not: testing boolean truth statements where you have an outcome but you wanted the opposite result. not(False) would be True if the statement being tested came out as True.
```

*Precedence* is set as below of which is evaluated first. For example with nested parenthesis and evaluating the *innermost* parenthesis first

```python
not (not (46>25) and (5>6 or 6<3)) and (5<3 or not (3<5))
```

The overall statement returns False

`Precedence in order to evaluate: not>and>or`

## Strings

We can make changes to concatination

Ask for the **Length**

```python
len('eric')
#asking for the length of a string will also count any blank spaces
```

Ask for a **Slice**

***Note***: As with python beginning with index **i** and ends with **j**, the *roof* of this slice is **j** and is not included in the slice i.e s[i:j-1]. So we can say python is ***inclusive exlusive*** as we include the first index element and exclude the last index element

```python
name = 'eric'
name[0]
#Will print the 0th digit in the variable/string, for example it will produce 'e'
#In python, the count begins from 0
```

Another example of different ways you can *slice*

```python
s = 'Python is Fun!'
s[1:5]
#returns: 'ytho'
s[:5]
#returns: 'Pytho'
s[1:]
#returns: 'ython is Fun!'
s[:]
#returns: 'Python is Fun!'
```

You can also *add* a third parameter to your slicing, **k** that represents the **Step Size** that you want to increment by:

```python
s[i:j:k]
#This gives a slice of the string from index i to index j-1, with a step size k
#Step size being the size of each iterative jump

s = 'Python is Fun!'
s[1:12:2]
#returns 'yhni u'
s[1:12:3]
#returns: 'yoiF'
s[::2]
#returns: 'Pto sFn'
s[::-1]
#returns: '!nuF si nohtyP'
```

## Python 'in' operator

The operators **in** and **not in** test for *collection membership*

Say we had a collection 'coll' with a list, or tuple, or dictionary

```python
element in coll
#tests if 'element' is absent or within the variable 'coll'
#Evaluations to True or False otherwise

element not in coll
#Same evaluation to see if element is a member of 'coll' but evaluates to False or True otherwise

equivalant expression to
not (element in coll)
```

## Input/Output

With print statements as well as input statements.

**input** expects the value entered by the user to be a string.

We would need to remember that if we want to use it as an integer then we would need to convert after receiving the input.

```python
number = int(input('type something here: '))
print(5 * number)
# This converts the input provided and casts it into a **integer** type for our purposes or uses later.
```

## While Statements

if the condition is true, then execute the code and go back to check the condition. Continue to do the condition until that condition is false.

This includes conditions with multiple parameters such as **and**, **or**, **not** etc and other such statements. If it evaluates to True, then it will complete the code and go back up the top.

```python
x = 6
while (x<8):
    print('hello')
    else:
        print('goodbye')
#it will continue to complete the while loop print function until x is equal or greater then 8. At that point it will no longer be a True statement so it will skip and go to the else statement to complete the False pathway
```

Another example of using a while loop to add numbers together from a starting point and the end being a variable that can easily be changed

```python
end = 6
n = 0
total = 0
while n <= end:
    total += n
    n += 1
print(total)
#This will produce the combination of adding each value from 1 through to 6 iteratively.
```

Or decreasing in values as you go down from a starting point

```python
number = 10
while number:
    if number > 0:
        print(number)
        number -= 2
```

Squaring a number using variables to hold memory and a while loop to iterate.

The following also shows the process of assigning variables outside of the **while loop** and then amending the variables inside the **while loop**. If we dont make changes to the variables inside the **while loop** then it will continue to grab the default assignments and not evaluate to the conclusion you want

```python
x = 3
answer = 0
iterationsleft = x #we are assigning the iterations we want to run through as a separate variable so that we can make changes in the loop to this variable without affecting **x**

while (interationsleft != 0):
    answer = answer + x
    iterationsleft = iterationsleft - 1
print (str(x) + '*' + str(x) + ' = ' + str(answer))
```

This code will step into the while loop, check if iterations is **0**. If not, then it will run the code until iterations is *equal to 0*. Meanwhile the variable **answer** is changed as we repeat the loop each time and **iterationsleft** is reduced for each repeated loop. This way our **x** variable remains unchanged and as **answer** gets adjusted by adding in **x** again, this way we are adding **x** to itself for **x** amount of times: Thereby ***squaring*** the number.

## For Loop Statements

```python
for n in range(5)
# range will give us back the integers 0 though to and up till 5 but not including 5.
```

You can also use *slices* and *indices* within the for loop

```python
for n in range(5:11:2)
# will complete the range starting at 5 and increment by 2 until we reach 11 but not including 11.
```

Similarly you can use the For loop in the following manner:

```python
for i in range(0,10,2):
    print(i)
# which will print 0, 2, 4, 6, 8 but not 10

for i in range(10,0,-2):
    print(i)
#prints 10, 8, 6, 4, 2 but not 0
```

If you are given some variable that you need to combine or use and the variable is scalable and without your code breaking and you want to include the end-value **somenumber**

```python
somenumber = 10
total = 0
for i in range(1,somenumber+1):
    total += i
print(total)
#this will run through the numbers and add each number to the **total** and this will also be inclusive of the end index **somenumber**
```

## Break Statement

Using a statement to break out of some code at a certain point
For example, if I evaluate something as **True** and no longer want to continue the code, **Break** provides a natural way to get out of the loop

```python
mysum = 0
for i in range(5:11:2):
    mysum += i
    if mysum == 5:
        break

print(mysum)
# This code says, if mysum == 5 then we want to stop the loop. As this range starts with the number 5, mysum is increased by i(5) and then the if statement evaluates to True; so we break
```

## Modulus division

Modulus division is an easy way to test for even or odd numbers.
The mod sign % used in a test has the following general english explanation:

```python
0 % 2
# The number 2 (on the right) goes into the number 0 (on the left) exactly 0 times (x amount of times). Afterwards there is 0 remaining.
2 % 2
# 2 goes into the number 2 exactly one time and there is 0 remaining.
3 % 2
# 2 goes into the number 3 exactly one time and there is 1 remaining.
23 % 5
# 5 goes into the number 23 example four times and there is 3 remaining.
```

Using this technique you can test for even numbers by using **mod** division and it will determine if the number is able to be evenly split, thereby being **even**.

## abs() Function

### *abs(number)*

Used to return the absolute value of a number.
It can be integer, a floating point number or complex number.

```python
float = -54.22
print('absolute value of this float is: ', abs(float))
# prints 54.22
integer = -88
print('absolute value of this intege is: ', abs(integer))
#prints 88
complex = 3-4j
print('absolute value or magnitude of complex is: ', abs(complex))
#prints 5.0
```

## Bisectional Searching

if you are trying to find a specific number and you know the beginning and end parameters then bisectional search is a great way to efficiently and effectively reach the outcome. Each step you are halving the available data and then you continue to repeat the step until you have found your answer.

### *This is really powerful as the computation time is dramatically reduced by halving and throwing away the data we dont need*

```python
x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
# high is initialised as our guess x = 25
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' High = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to a square root of ' + str(x))
```

## Call/Invoke a Function

Functions take a set of parameters; the number can be 0 and the parameters are set inside the function.

```python
def is_even (i): #keyword || name || parameters or arguments
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise false
    """
    print('hi')
    return i % 2 == 0

is_even(3) # calling the function using its name and values for parameters.

# as per the function if we assign i = 3 as per the call, then we replace all i's with 3.
```
### Returning a function

Instead of invoking and calling a function. You can have another function *return* a function.
You can imagine it follows as such: when *returning* a function by **not** providing parameters at all (parenthesis), then we are not asking for **that function we are returning** to return any *result*. Instead the function call will return a function and this new function returned is going to take the place of the entire intial function call

```python
def add (x,y):
    return x + y
def times(x,y):
    return x*y
def add_or_times (a):
    if a > 5:
        return add #returning a function but not calling on the function with parameters
    else:
        return times
# for example:
add_or_times(6)(3,1)
#great than 5
#return add
add(3,1)
>>>4
#so we can see we replaced our initial function with the returned function but then we ran the parameters using that new function
```

### *Some rules for functions*

* Only one **return** will be completed as the **return** order throws you outside of the function.
* Any code inside of the function but **after** the **return** statement will be ignored.
* If you dont have an explicit return given inside the function, then it will return the value **None**
* Value is given to the function caller, so functions have a value associated with it

### Scopes inside scopes inside scopes, scopes all the way down

Sometimes called an internal or helper function. It only belongs inside and to the function that we called. It's protected.

```python
def scope_one():
    def scope_two():
        print('a')

    x = 3
    y = 'and so forth'
```

## Inheritance

Taking on the variables and set parameters from previous (higher) scopes that sit in a hierachy. As we progress down the rabbit hole with new scopes, the inheritance of the previous scopes follow through.

```python
def g(x):
    def h():
        x = 'abc'
        #note there is no return statement so this variable is not returned to x
    x = x + 1
    print('in g(x): x =', x)
    h() #calling that h() function now and creating that new scope
    return x

x = 3
z = g(x)
```

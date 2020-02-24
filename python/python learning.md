# Python Learning

## Table of Contents

- [Python Learning](#python-learning)
  - [Table of Contents](#table-of-contents)
  - [IF Statements](#if-statements)
  - [AND, OR, NOT](#and-or-not)
  - [Strings](#strings)
  - [Python 'in' operator](#python-in-operator)
  - [Input/Output](#inputoutput)
  - [While Statements](#while-statements)
  - [For Loop Statements](#for-loop-statements)
  - [Break Statement](#break-statement)
  - [Modulus division](#modulus-division)
  - [abs() Function](#abs-function)
  - [Bisectional Searching](#bisectional-searching)
  - [Call/Invoke a Function](#callinvoke-a-function)
    - [Returning a function](#returning-a-function)
    - [*Some rules for functions*](#some-rules-for-functions)
    - [Scopes inside scopes inside scopes, scopes all the way down](#scopes-inside-scopes-inside-scopes-scopes-all-the-way-down)
  - [Inheritance](#inheritance)
  - [Recursion](#recursion)
    - [*Some rules*](#some-rules)
  - [Modules and Files](#modules-and-files)
    - [File handle](#file-handle)
  - [Tuples, List, Mutability, Cloning](#tuples-list-mutability-cloning)
    - [Tuples ()](#tuples)
    - [List []](#list)
    - [Operations on Lists](#operations-on-lists)
      - [Convert a List to Strings and back](#convert-a-list-to-strings-and-back)
    - [Other Operations](#other-operations)
    - [Bringing it all together: LOOPS, FUNCTIONS, range, and LISTS](#bringing-it-all-together-loops-functions-range-and-lists)
  - [Mutation, Aliasing, Cloning](#mutation-aliasing-cloning)
    - [Mutation and Iteration](#mutation-and-iteration)
  - [Functions as Objects](#functions-as-objects)
    - [HOPS Higher Order Procedure](#hops-higher-order-procedure)
      - [Map](#map)
  - [Dictionaries](#dictionaries)
    - [List Comprehension and Dictionary Comprehension](#list-comprehension-and-dictionary-comprehension)
      - [List Comprehension](#list-comprehension)
      - [List comprehension with all()](#list-comprehension-with-all)
      - [List comprehension with set()](#list-comprehension-with-set)
      - [Dictionary Comprehension](#dictionary-comprehension)
  - [Global Variables](#global-variables)
    - [Fibonacci numbers using if statements and recursion versus dictionary and recursion](#fibonacci-numbers-using-if-statements-and-recursion-versus-dictionary-and-recursion)
  - [Testing and Debugging](#testing-and-debugging)
    - [Unit Testing](#unit-testing)
    - [Regression Testing](#regression-testing)
    - [Integration testing](#integration-testing)
    - [Black Box Testing](#black-box-testing)
      - [Summary (Black Box Testing)](#summary-black-box-testing)
    - [Glass Box Testing](#glass-box-testing)
      - [Summary (Glass Box Testing)](#summary-glass-box-testing)
    - [Debugging](#debugging)
      - [Error Messages](#error-messages)
    - [Print Statement Debugging](#print-statement-debugging)

This is not an indepth look into each topic but rather just reminders or bits of info to cover my gaps in knowledge

## IF Statements

```python
if true then proceed to this code
elif Else this code
elif Else this code
else If nothing Else then proceed to this code
```

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

## Input/Output

With print statements as well as input statements.

**input** expects the value entered by the user to be a string.

We would need to remember that if we want to use it as an integer then we would need to convert after receiving the input.

```python
number = int(input('type something here: '))
print(5 * number)
# This converts the input provided and casts it into a **integer** type for our purposes or uses later.
```

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

## abs() Function

Syntax follows the `abs(number)` format.

- Used to return the absolute value of a number
- It can be integer, a floating point number or complex number

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

[Back to Top](#table-of-contents)

## Bisectional Searching

if you are trying to find a specific number and you know the beginning and end parameters then bisectional search is a great way to efficiently and effectively reach the outcome. Each step you are halving the available data and then you continue to repeat the step until you have found your answer.

This is really powerful as the computation time is dramatically reduced by halving and throwing away the data we dont need

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

[Back to Top](#table-of-contents)

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

- Only one **return** will be completed as the **return** order throws you outside of the function.
- Any code inside of the function but **after** the **return** statement will be ignored.
- If you dont have an explicit return given inside the function, then it will return the value **None**
- Value is given to the function caller, so functions have a value associated with it

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

[Back to Top](#table-of-contents)

## Recursion

Design solutions to problems by breaking it up into pieces that you can use.

[Back to Top](#table-of-contents)

### *Some rules*

- Each recursive call to a function creates its own scope/environment
- Bindings of variables in a scope is not changed by recursive call
- flow of controll passes back to previous scope once function call returns value
- Figure out what *Base Case* to use - i.e what is the bottom line.
- Within recursion you won't have conditions to meet that will break you out of the loop. Therefore its important to make sure that you are **changing** the parameter so that you meet the base case. i.e you are running each successive recursion, with a smaller version of the parameter. Eventually hitting a floor, and your **test case**.

```python
def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)
```

We can also recursively solve characters or strings instead of only numbers. For example solving for a **palindrom** whereby the string reads left the same as it reads right (backwards).

```python
#step 1 write function to convert string into useable characters
#step 2 recursive solution for checking first  and last
#step 3 call on palindrom function then call function for converting string.
#bundle this up into a single function or template is_palindrome (s)
def is_palindrome (s):
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
                # purpose here is to convert a string or sentence into just its character form, thereby removing any spaces, special characters and numbers and converting it all the lower case.
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
            #purpose here is to test if the first letter and the last letter are equal and then to call on the function again recursively doing so on the remaining letters until we get a length of 1 or 0 letters (which is 100% a palindrome.

    return is_pal(to_chars(s)) # calling on the is_pal recursion and instead of doing it directly on the string; we call it on our function that converts the string into something useable.

print(is_palindrome('are weew era'))
```

## Modules and Files

Modules is a .py file containing a collection of Python definitions and statements.

You can import these .py files into the shell or into some other file if we want to use it there.

Invoking the module:

Inside some filename.py, we can define the variable pi = 3.14159 and have the definitions inside there be consistent with the variable we have there.

In another file, we can import this file to use the definitions and code there within.

```python
import filename
pi = 3
print(pi)
>>>3
print(filename.pi)
>>>3.14159
print(filename.some_definition(3)))
>>>will do the calculation based on using filename and applying it to the number we passed it
```

With the above code it means if we want to use the definitions or code from the file, we would need to append or use the **filename.*whatever*** in order to use the code inside the filename.

Another option if we don't want to refer to variables by their module i.e **filename.*area*** or **filename.*variable_name***; we can use the:

```python
from filename import *
```

This has the effect of creating bindings within our current shell or scope for all objects defined inside **filename**

[Back to Top](#table-of-contents)

### File handle

handling of files or many files.py is important if you are going to sync across them or have different features/products inside each file but you want to draw of each other.

With the internal file handling, it doesn't require the operating system and can be done through various functions and options such as below

```python
name_handle = open('kids', 'w')


#open is going to open up a file - access into a file.
#the 'w' is for writing *directly* into it.

name_handle.close()
# The closed parenthesis shows we are *invoking* the close of the file.
#When done I can close the file. shut up shop
```

There are some additional modularity such as **r** for only reading the file and as such can print lines or details from a file.

## Tuples, List, Mutability, Cloning

[Back to Top](#table-of-contents)

### Tuples ()

Tuple is an ordered sequence of elements. They are **immutable**; they cannot be change inside the Tuple.

```python
Tuples make use of *parenthesis* () for values inside tuples
```

We cannot change the inner pieces of a Tuple, similar to how strings are immutable. We can add to it, we can splice it, but we cannot change the values.
Tuples are also **Iterable** so it means you can walk down the tuple and use each value how you would like.

```python
for Tuples with only **1** element then you will make use of the comma in order to form a correct Tuple.
x = (1,) = Tuple
x = (1) = Int
However if the Tuple has multiple elements then you don't need to use the comma at the end to form a Tuple
x = (1, 2, 3) = Tuple
```

### List []

Big difference between **Tuples** and **Lists** is that the **Lists** are mutable; they can be changed.

Lists containts elements, normally all of 1 type such as *all integers* or rarely mixed elements.

They are also accessible by index, so you can do all the usual tests

- len(List) # Get a length
- List[0] # Find the index
- List[2] + 1 # Find the index and do something to it
- List[3] # Go outside the list range and get errors

The important distinction is that a List is mutable so we can perform the following

- List[1] == 5 # changing index 1 to the integer 5

### Operations on Lists

Certain operations we can do with lists. As with lists, they are mutable so once you use operations on lists, it will change that variable or that list permanently.

- The dot tells python to *get out some **method***

```python
List.append(n) # we can append or add another element to the list.
List.extend[0,2] # Take a list and add to the end of it. Does not return anything until you call on the list
del(List[1]) # to remove the element at index 1.
pop(List)# Remove from the **end** of the list and returns the removed element
List.remove(element) # a specific element by looking for the element and removes it, if multiple occurances then it will remove the first. If element not in the list then it will give an error.
ListAB = ListA + ListB # We can concatenate two lists ListOne + ListTwo
```

#### Convert a List to Strings and back

```python
list(s) # returns a list with every character from s an element in the list\
s.split() # Split the string on a character
s.split('<') # Split at this character
''.join(list) # Will join all the characters i nthe list to produce a string
'_'.join(list) # will do the same but place the special character '_' between each element of the list.
```

### Other Operations

sorted() does not mutate the list while the **method** sort() mutates the list

```python
sorted(List) # returns a sorted version of List. Provides a sorted version of List but does not mutate it
List.sort() # empty parenthesis to say invoke the function And this will mutate the List to be ordered
List.reverse() # empty parenthesis to invoke the call. and this will mutate the list.
List.insert(index, element) # inserting an element at the nth index. Returns none as it doesnt return anything
List.count(element) # counts number of occurences. returns number
```

### Bringing it all together: LOOPS, FUNCTIONS, range, and LISTS

range is a special procedure and actually returns something that behaves like a **Tuple**

For example  range(5) would bring a ***List*** [0, 1, 2, 3, 4].

So this means you can think of it like a list similar to how you would slice or call on it. i.e range(5, 2, -1) using the step and going backwards and such.

## Mutation, Aliasing, Cloning

We need to be careful with variables with lists that we assign: assigning them to directly to each others list means if its mutated, it will affect both variables.

```python
variable = ['sunny', 'windy', 'rainy']
weather = variable
# This points to the same list in the internal computer memory we have allocated. So if we change the list, it affects both variables and this may have unexpected consequences
```

Making a clone of this variable is easier in order to set up separate lists inside the memory allocation

```python
variable = ['sunny', 'windy', 'rainy']
weather = variable[:]
# this difference is that we are cloning and greater a second list for the variable *weather* so that each variable points to its own list.
```

Cloning is useful when I want to do something to a list that involves mutation but doesnt affect the original list.

[Back to Top](#table-of-contents)

### Mutation and Iteration

When iterating over a list, python will adjust and mutate the list as it proceeds with each variable. So if you give it instructions to remove a value at nth index. Then python may not behave like you think because as it removes an *element*; the list becomes smaller -1 on the next iteration and the next step that was supposed to be at index [2], the element [3] has now moved down to [2] and the original [2] has moved down to [1] thereby the code **skipping** 1 element.  

Cloning lists is the best way to iterate correctly and keep python on track with each iteration

```python
def removeDuplicate(List1, List2):
    List1_Copy = List1[:] # create a clone of List1
    for e in List1_Copy:
        if e in List2:
            List1.remove(e) # Thereby iterate over each element in Copy, if the value is in List 2, then we remove it from List 1 and mutate the original: remove the duplicates
```

## Functions as Objects

Functions are **first class objects** in saying that they :

- Have types
- can be elements of data structures like lists
- can appear in expressions (as part of an assignment statement and as an argument to a function)

Functions are particularly usefules as arguments when coupled with lists known as **higher order programming**

```python
def applyToEach(List,Function):
    for i in range(len(List)):
        L[i] = function(List[i]) # for each index I get out of the list, apply the function to it; then put it back into the list and replace that original [i]
# This will cycle through the list and at each index, apply the function and return it back to the list.
# The list is amended and replaced with the function-applied index.
List = [1, -2, 3.4]
applyToEach(List,abs)
# returns [1, 2, 3.4]
applyToEach(List,int)
# return [1, 2, 3]
applyToEach (List, fact) #factorial function that we defined earlier on
# returns [1, 2, 6]
applyToEach(List, fib) #fibonacci function that we defined earlier on
# returns [1, 2, 13]
```

In the reverse as well

```python
def applyFunctions(List, x):
    for function in List:
        print(function(x))

applyFunctions([abs int, fact, fib], 4) # we provide a list of functions that we can to invoke in place of *List* and then apply those functions to the number 4 that we pass in
#returns
#4
#4
#24
#5
```

[Back to Top](#table-of-contents)

### HOPS Higher Order Procedure

#### Map

```python
map(abs, [1, -2, 3, -4])
# map will walk down the list provided in the argument and apply the function to each element. and allow us to print the outcome
for elt in map(abs, [1, -2, 3, -4]):
    print(elt)

#returns [1, 2, 3, 4]
```

There is a difference here between what we did before; applying the functions to the index elements that we pull out and then we put the mutated elements back to that list

That list always pointed to the same list in the memory so we are mutating that list with each iteration.

By contrast, map gives me back a structure that acts like a list that I have to walk back out to get what I want; printing it out or using it.

**map** can also be used to run down more than 1 list, apply a function to each item in each list and produce an outcome taking the **whole** data in to account

```python
list1 = [1, 28, 54]
list2 = [2, 34, 17]
for elt in map(min, list1, list2):
    print(elt)
#Returns the minimum of each index compared. so Index [0] for each list, the minimum is 1. For index [1] for each list, the minimum is 28 and for index [2] for each list, the minimum is 17
#returns [1, 28, 17]
```

## Dictionaries

With lists, you operate on a index starting at 0, and you have a element assigned to that index. as you walk through the list, the index and the element correspond to the place it is currently in the list

With **dictionaries**, we have what is referred as ***keys*** and instead of asking for a zeroth element or ith element; we are going to say, *"give me the element associated with this key"*.

I can look up a **key** and retrieve all information associated with that **key**

```python
my_dictionary = {}
#creating empty dictionary
grades = {'Ana':'B', 'John':'A+', 'Casey':'C-'}
grades['John']
# Will return 'A+'
grades ['Sylvan'] = 'A'
# Will add a new entry into that dictionary
'John' in grades
# will return True or False if the key is in the dictionary
del[grades['Ana']]
# Deletes an entry
grades.keys() #because its a method, open&close parenthesis calls the method
# Returns an iterable of all keys, I can walk down all the collection of values and do something to them
grades.values()
# Returns an iterable of all values, I can walk down all the collection of values and do something to them
```

- Values = They can be anything, lists or even other dictionaries
- Keys = Must be unique, Immutable type (int, float, string, tuple, bool)
- Careful with using float type because if the float has a rounding or accuracy issue then we may no find the key associated with it
- Dictionaries has no order guaranteed. Your **keys** are your calling cards and should not be thought of in terms of using indices to call positional elements.

[Back to Top](#table-of-contents)

### List Comprehension and Dictionary Comprehension

List comprehension and by extention dictionary comprehension is a great way of making readable, compact way of creating lists or dictionaries. Merging several lines into a single line that indicates which elements should be added to the list.

#### List Comprehension

```python
list = []
for i in range(15):
    if i % 2 == 0:
        list.append(i)
```

and then using **list comprehension**

```python

list = [i for i in range(15) if i % 2 == 0]
# syntax being [value we return to list] for [element] in [sequence] if [condition]
# so we iterate every each value from 0 to 14 but not including 15 and if the [condition] is met, the integer meets the criteria, then include the [value we return to the list] in the final list
```

For the above code:

- the **condition** is optional as we can simply *i for i in range(15)* and return all integers into a list.
- Not restricted to just integers, we can also have expressions to alter the [i] indices

```python
list = [i*3 for i in range(15) if i%2 == 0]
# iterates over 0 - 14 and selects all *even* but we mutate the index value at each iteration.
# if called, returns [0, 6, 12, 18, 24, 30, 36, 42]

list = [value for value in namesDict.values() if value % 2 != 0]
# depending on what is in the dictionary, we can iterate over each **value** in the dictionary and use the values to test the if [condition] then select those and assign them to the *list*

#another example
secretWord = 'durian'
lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']

    return len(("".join(char for char in lettersGuessed if char in secretWord))) == len(secretWord)

```

#### List comprehension with all()

The all() method returns True boolean if all elements within an iterable is True otherwise it returns False

Syntax `all (iterable)`

```python
secretWord = 'durian'
lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']

    all(c in lettersGuessed for c in secretWord)
    # single liner using list comprehension rules to produce a boolean returned.
    >>> True
```

#### List comprehension with set()

Basic uses of set() includes membership testing and eliminating duplicate entries

curly braces or the set() function can be used to creat sets.
Note: to create an empty set, you have to use set(). Curly braces will only create an empty dictionary

```python
secretWord = 'durian'
lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']

set(lettersGuessed) >= set(secretWord)
#or
set(c for c in lettersGuessed if c in secretWord)
# returns {'a', 'd', 'i', 'n', 'r', 'u'} just need to compare the set to secretWord
```

#### Dictionary Comprehension

Python allows you to create new dictionaries from existing ones but assigning **different** ***values***

```python
dictionary = {key:new_vlaue for (key, value) in dictionary.items()}
# iterates over the keys and values in a dictionary and adds the corresponding key and new value that is the result of an expression
```

For example for the following dictionary:

```python
grades = {"Nora": 90, "Lulu": 15, "Gino": 60}
doubleGrades = {key: value*2 for (key, value) in grades.items()}
doubleGrades
# returns {'Nora': 180, 'Lulu': 30, 'Gino': 120}
```

You can also use **conditions** in dictionary comprehension

```python
grades = {"Nora": 90, "Lulu": 15, "Gino": 60}
doubleGrades = {key: value*2 for (key, value) in grades.items() if value % 2 == 0}
# selects only *even* if the **original** value was even
doubleGrades
# returns {'Nora': 180, 'Gino': 120}
```

## Global Variables

Convenient when we want to keep track of information inside of a function

Dangerous because:

- Breaks the scoping of variables by function call
- side effects unseen in your code by affecting the global scope

**global** can be used by making the function or variables accessible **outside** of your define functions.

[Back to Top](#table-of-contents)

### Fibonacci numbers using if statements and recursion versus dictionary and recursion

```python
numFibCalls = 0 # initialise our counter
def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return n
    #both base cases checked!
    else:
        return fib(n-1) + fib(n-2)

print(fib(12))
print('Number of times the function is called: ', numFibCalls)

# 144
# Number of times the function is called:  465
```

and dictionary

```python
numFibCalls = 0
def fibefficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fibefficient(n-1, d) + fibefficient(n-2, d)
        d[n] = ans
        return ans

d = {0:0, 1:1}
print(fibefficient(12,d))
print('Number of times the function is called: ', numFibCalls)

# 144
# Number of times the function is called:  23
```

## Testing and Debugging

Design code that can easily test and debugged by breaking up the code into simplified modules that allows you to test each module to the design of how you wanted it to function.

[Back to Top](#table-of-contents)

### Unit Testing

- Take each piece of program and validate it
- testing each function separately

### Regression Testing

- Add test for bugs as you find them in a function
- Catch reintroduced errors that were previously fixed

### Integration testing

- Does overall program work?

### Black Box Testing

Testing by going through the specifications to realise any potential bugs. This method is designed to be done without looking at the code

#### Summary (Black Box Testing)

- designed without looking at the code
- Just look at the specifications
- Explore paths through specifications
  - Empty list, list of 1 and list of many and so on
  - What if I have any extreme cases of really large numbers, or really small numbers
  - Testing floats and negatives if the specifications shows its designed for it

### Glass Box Testing

Testing by going through the **code** and following the available paths to reach potential bugs. This method is designed to just complete the grunt work.

For example:

```python
def abs(x):
    """ Assumes x is an int
    returns x if x>=0 and -x otherwise"""
    if x < -1:
        return -x
    else:
        return x
```

The above code shows that path-complete tests could *miss a bug*, using path-complete testing such as **abs(2)** or **abs(-2)** would test each path however if you failed to complete boundary case testing then you would miss that **abs(-1)** incorrectly returns **-1**

#### Summary (Glass Box Testing)

- Designed with looking at the code
- Use code directly to guide design of test cases
- **path-complete** if every potential path through code is tested at least once
- ***Drawbacks include:***
  - can go through loops arbitrarily many times
  - missing paths
- ***Guidelines***
  - **branches** - exercise all parts of a conditional
  - **for loops** - loop not entered; body of loop executed exactly once; body of loop executed more than once
  - **while loops** - same as **for loops**, cases that catch all ways to exit loop

### Debugging

#### Error Messages

- **IndexError**
  - trying to access beyond the limits of a list
  - `test = [1,2,3]`
  - `test[4]`
- **TypeError**
  - trying to convert an inappropriate type
  - `int(test)`
- **NameError**
  - referencing a non-existing variable
  - `a`
- **TypeError**
  - Mixing data types without appropriate coercion
  - `'3'/4`
- **SyntaxError**
  - forgetting to close parenthesis, quotation etc
  - `a = len([1, 2, 3, 4]`
  - `print a`

### Print Statement Debugging

Print statements are great for debugging, use the following steps to break it down:

- Print when you enter a function
- Print out the values of the parameter - Make sure they are what you expect.
- Print Result to check if its expected
- Bisection method used to debugging - Place the print statement in the middle of the code\
and work through and see if the bug is higher or lower


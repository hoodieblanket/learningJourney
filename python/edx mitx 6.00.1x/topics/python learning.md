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

    Precedence: not>and>or

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

With print statements as well as input statements. **input** expects the value entered by the user to be a *string*. We would need to remember that if we want to use it as an integer then we would need to convert after receiving the input.

```python
number = int(input('type something here: '))
print(5 * number)
# This converts the input provided and casts it into a **integer** type for our purposes or uses later.
```

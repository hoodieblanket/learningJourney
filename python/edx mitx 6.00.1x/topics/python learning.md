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
## For Loop Statements

```python
for n in range(5)
# range will give us back the integers 0 though to and up till 5 but not including 5.
```

You can also use slices and indices within the for loop

```python
for n in range(5:11:2)
# will complete the range starting at 5 and increment by 2 until we reach 11 but not including 11.
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
# This code says, if mysum == 5 then we want to stop the loop. As this range range starts with the number 5, mysum is increased by i(5) and then the if statement evaluates to True; so we break
```


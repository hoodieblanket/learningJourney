# Python Learning

## IF Statements

```python
if true then proceed to this code
elif Else this code
elif Else this code
else If nothing Else then procced to this
```

## AND, OR, NOT

```python
and: used for boolean tests where you have two outcomes and determining if they are True or False statements to reach an 'overall' True or False
or: testing between two Truth statements and if EITHER of them are True then the overall test is that atleast one is True
not: testing boolean truth statements where you have an outcome but you wanted the opposite result. not(False) would be True if the statement being tested came out as True.
```

*Precedence* is set as below of which is evaluated first. For example with nested parenthesis and evaluating the *innermost* parenthesis first

    not (not (46>25) and (5>6 or 6<3)) and (5<3 or not (3<5))

The overall statement returns False

    Precedence: not>and>or

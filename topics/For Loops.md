# For Loops


## the longest alphabetical substring inside a string. 
    Create the variables I want to compare and contain the values outside the loop.
    The alphabet has boolean values `a < b` is `True` and `e < c` is `False` which makes it simple to compare each letter in the string - Alphabetical is the same as smallest to largest.   
    So using the comparison operators `< > == etc.` I can compare to see if I have a string going in a row.

***


```python
s = 'azcbobobegghaklabcdefghij'

previousAttempt = ""
currentAttempt = ""
longestString = ""

for char in s:
    if previousAttempt <= char:
        currentAttempt += char
        if len(currentAttempt) > len(longestString):
            longestString = currentAttempt
    else:
        currentAttempt = char
    previousAttempt = char




print("Longest substring in alphabetical order is: " + longestString)
```

output `Longest substring in alphabetical order is: abcdefghij`

***
 * `previousAttempt = ""` is used to compare additional iterations through the `for loop` so that the current iteration for `char` is compared and evaluated.
 * `currentAttempt = ""` is used to combine the all the correct conditions together
 * `if len(currentAttempt) > len(longestString)` is used to evaluate the length of the conditions. e.g 4 characters `abcd` is greater than 2 characters `ab` so if `currentAttempt` is more than `longestString` then it will boot the old attempt out and use the new value.
 * if `previousAttempt` is **not** <= char then we redefine `currentAttempt = char` which just makes the currentAttempt variable become equal to the iteration of `char` we just used (instead of the combined collection if the `if` condition was successful)
 * `previousAttempt = char` is used to keep track of the current attempt in the iterations `e.g having used "c" or "d"`. As we roll through the `for loop`, we can then keep comparing the `char` to `previousAttempt` to start working towards an **alphabetical** substring


## Finding the number of times a Substring appears inside a String

    Need a variable to `total` the number of times we find a substring
    using the `len()` function we can convert the string to its length.
    
***
```python
s = 'azcbobobegghakl'

total = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        total +=1

print("Number of times bob occurs is: " + str(total))
```
Output: `Number of times bob occurs is: 2`
***
* `for i in range(len(s)):` this loops runs through and converts the string to its length (15)
* `if s[i:i+3] == "bob"` s = string so this is indexing the string through each iteration (0, 1, 2, 3). 
* as its indexing and checking, its going through iterations and checking for "bob". e.g it starts at [0] then checks [0] : [3] for "bob"
* then it goes [1] and checks [1] : [4] etc..
* This overlaps the letters so strings might have bobobob and it still finds all 3.

e.g

 (0) |(1)|(2)|(3)
---|---|---|---
B?|O?|B?||
(blank)|B?|O?|B?

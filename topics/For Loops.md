# For Loops


Below is for finding the longest alphabetical substring inside a string. 
   first I create the variables I want to compare and to contain the iterations
   I had to realise that the alphabet has boolean values `a < b` is `True` and `e < c` is `False`
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

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
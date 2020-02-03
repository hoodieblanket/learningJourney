s = 'azcbobobegghaklabcdefghij'

previousAttempt = ""
currentAttempt = ""
longestString = ""

for char in s: 
    #iterate through each character in the string
    if previousAttempt <= char:
        #test is the character assigned to (previousAttempt) is alphabetically less than or equal to the character
        currentAttempt += char 
        #If the condition is true, then add the character to (currentAttempt)
        if len(currentAttempt) > len(longestString):
            # test if the length of currrentAttempt is greater than the longestString that we have saved so far.
            longestString = currentAttempt 
            #if true condition then the string is to be updated for our new longestString so far.
    else:
        currentAttempt = char 
        # reset currentAttempt back to character
    previousAttempt = char 
    # reset previousAttempt back to character





print("Longest substring in alphabetical order is: " + longestString)

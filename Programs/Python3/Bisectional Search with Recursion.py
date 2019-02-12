def isIn(char,aStr):
    '''
    char: a letter
    aStr: a string of letters
    '''
    #in order to make sure we place the string in alphabetical order we can use the following:
    aStr = ''.join(sorted(aStr))
    #we want to assign the value from the bisectional search to a variable so we can test cases. i.e the below
    #will produce the middle of the string of letters, i.e "n" and then ask if n == char or else do code
    m = aStr[len(aStr) // 2]
    # for recursion, what is the base case or smallest case that is likely to happen
    if m == '':
        return False
    # to capture if the string is None ''
    if m == char:
        return True
    elif aStr == '' or len(aStr) == 1:
        return False
    else:
        if char < m:
            return isIn(char,aStr[:len(aStr) // 2])
        elif char > m:
            return isIn(char,aStr[len(aStr) // 2:])

isIn("r","abcdefghijklmnopqrstuvwxyz")

print(isIn("r","abcdefghijklmnopqrstuvwxyz"))
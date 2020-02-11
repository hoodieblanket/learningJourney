#bisectional searching for strings without using the *in* or *not in* functions

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    aStr = sorted(aStr)
    middle = int(len(aStr)/2)
    
    if not aStr:
        return False

    else:
        if aStr[middle] != char:
            if len(aStr) < 2:
                    return False
            elif char < aStr[middle]:
                aStr = aStr[0:middle]
                return isIn(char,aStr)
            elif char > aStr[middle]:
                aStr = aStr[middle:]
                return isIn(char,aStr)
        else:
            return True

aStr = 'abcdefghijklmnop'
print(isIn('f',aStr))
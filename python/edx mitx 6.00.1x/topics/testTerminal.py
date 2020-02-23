def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    empty = ''
    for l in lettersGuessed:
        if l in secretWord:
            emptyVariable += l
        else:
            continue
    
    if len(emptyVariable) == len(secretWord):
        return True
    else:
        return False





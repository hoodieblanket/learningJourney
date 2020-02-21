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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #list comprehension
    # 
    bilbo = [c for c in lettersGuessed if c in secretWord]
    return len(bilbo) == len(secretWord)
        
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # list comp # 2
    return len(("".join(char for char in lettersGuessed if char in secretWord))) == len(secretWord)
# the rnadom words have "x" letters
#what is your guess? 8 guesses allowed, 1 character allowed
# assign some empty variable
# while guesses > 0
    #do stuff
        #if secretword == variable:
            #print winner
            #print secret word
        #elif yes if the letter is in the secret word
            #do stuff
            # assign to variable
        #elifprevious letter
            # repeat instructions
            # dont lose guess
        #else:
            #do stuff
            #guesses -= 1
        #display current letters
#if out of guesses
        # end game
        # print secret word

import random

WORDLIST_FILENAME = "words.txt"
# if you get an error that it cannot find the above file. Then place the FULL directory linking to the file
# with all the words above.

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    sWord = ''
    for s in secretWord:
        if s in lettersGuessed:
            sWord = sWord + s
    if sWord != secretWord:
        return False
    else:
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    sWord = ''
    for s in secretWord:
        if s in lettersGuessed:
            sWord = sWord + s
        elif s not in lettersGuessed:
            sWord = sWord + '_ '
    return sWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    for s in lettersGuessed:
        allLetters = allLetters.replace(s, '')
    return allLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("-----------------------")
    print("Welcome to the game Hangman! \
    I am thinking of a word that is " + str(len(secretWord)) + " letters long")

    count = 8
    lettersGuessed = ['']

    while getGuessedWord(secretWord, lettersGuessed):
        print("-----------------------")
        print("You have " + str(count) + " guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        userGuess = input("Please guess a letter: ")
        if userGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + (getGuessedWord(secretWord, lettersGuessed)))
        elif userGuess in secretWord:
            lettersGuessed.append(userGuess)
            print("Good guess: " + (getGuessedWord(secretWord, lettersGuessed)))
            if str(getGuessedWord(secretWord, lettersGuessed)) == secretWord:
                print("-----------------------")
                print("Congratulations, you won!")
                break
            elif count == 0:
                print("Oh dear, you have run out of chances.")
                print('The End.')
                break
        elif userGuess not in secretWord:
            lettersGuessed.append(userGuess)
            print("Oops! That letter is not in my word: " + (getGuessedWord(secretWord, lettersGuessed)))
            count -= 1
            if count == 0:
                print("-----------------------")
                print("Sorry, you ran out of guesses. The word was " + secretWord)
                break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

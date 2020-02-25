# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/home/hoodie/Dropbox/coding/learningJourney/python/scripts/hangman/words.txt"

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
    return len(("".join(char for char in lettersGuessed if char in secretWord))) == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join(c if c in lettersGuessed else '_' for c in secretWord)

    #first attempt
    # sWord = ''
    # for s in secretWord:
    #     if s in lettersGuessed:
    #         sWord = sWord + s
    #     elif s not in lettersGuessed:
    #         sWord = sWord + '_ '
    # return sWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join(c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in lettersGuessed)
    #first attempt
    # allLetters = 'abcdefghijklmnopqrstuvwxyz'
    # for s in lettersGuessed:
    #     allLetters = allLetters.replace(s, '')
    # return allLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    guesses, guessed = 8, []
    while guesses > 0:
        ltrs = getAvailableLetters(guessed)
        print("---\n" "You have", guesses, "guesses left.\n")
        guess = input("Available letters: " + ltrs + "\nPlease guess a letter: ")
        if guess not in ltrs:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, guessed))
        else:
            guessed += [guess]
            if guess in secretWord:
                print('Good guess:', getGuessedWord(secretWord, guessed))
                if isWordGuessed(secretWord, guessed):
                    guesses = -2020
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, guessed))
                guesses -= 1
    print("---\n" "Congratulations, you won!") if guesses == -2020 else \
    print("---\n" "Sorry, you ran out of guesses. The word was " + secretWord + ".")

    # First attempt
    # print("-----------------------")
    # print("Welcome to the game Hangman! \
    # I am thinking of a word that is " + str(len(secretWord)) + " letters long")

    # count = 8
    # lettersGuessed = ['']

    # while getGuessedWord(secretWord, lettersGuessed):
    #     print("-----------------------")
    #     print("You have " + str(count) + " guesses left")
    #     print("Available Letters: " + getAvailableLetters(lettersGuessed))
    #     userGuess = input("Please guess a letter: ")
    #     if userGuess in lettersGuessed:
    #         print("Oops! You've already guessed that letter: " + (getGuessedWord(secretWord, lettersGuessed)))
    #     elif userGuess in secretWord:
    #         lettersGuessed.append(userGuess)
    #         print("Good guess: " + (getGuessedWord(secretWord, lettersGuessed)))
    #         if str(getGuessedWord(secretWord, lettersGuessed)) == secretWord:
    #             print("-----------------------")
    #             print("Congratulations, you won!")
    #             break
    #         elif count == 0:
    #             print("Oh dear, you have run out of chances.")
    #             print('The End.')
    #             break
    #     elif userGuess not in secretWord:
    #         lettersGuessed.append(userGuess)
    #         print("Oops! That letter is not in my word: " + (getGuessedWord(secretWord, lettersGuessed)))
    #         count -= 1
    #         if count == 0:
    #             print("-----------------------")
    #             print("Sorry, you ran out of guesses. The word was " + secretWord)
    #             break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

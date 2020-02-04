low = 0
high = 100
print("Please think of a number between 0 and 100")

while True:
    guess = int(high + low) //2
    print("Is your secret number: " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. \
            Enter 'l' to indicate the guess is too low. \
            Enter 'c' to indicate I guessed correctly:")
    if ans == "c":
        print("Game over. Your secret number is " + str(guess))
        break
    elif ans == "h":
        high = guess
    elif ans == "l":
        low = guess
    else:
        print("Sorry, I did not understand your input")


# Another way 

low = 0
high = 100
ans = (high + low)//2

print('Please think of a number between 0 and 100!')
print()
secretNumber = input('Please any key when you are ready\n')
while ans != secretNumber:
    ans = (high + low)//2
    inp = input('Is your secret number ' + str(ans) + '?\n' + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    print()
    if inp not in ('h', 'l', 'c'):
        print('Sorry, I did not understand your input.')
        print()
    elif inp == 'h':
        high = ans
    elif inp == 'l':
        low = ans
    elif inp == 'c':
        secretNumber = ans
        print('Game over. Your secret number was: ' + str(ans))
        print()
        break
    else:
        print('bug in the system')
    
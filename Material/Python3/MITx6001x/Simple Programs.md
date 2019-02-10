# Approximate Solutions
When you want to get *close* to the answer but because there is an infinite number of possibilities, this is the\
 next best option known as the **good enough solution**.
 
 ### Cube Root example
 ```python
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guess =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
    
```
`abs(n)` returns the absolute value.


The above code will work with most queries but the issues is; what happens if the guess falls just shy of the cube but\
the next iteration jumps over the cube? using `29` for the cube above will produce an infinite loop. 

It jumps over the cube and then the program just keeps going.\
This highlights the need to make sure you account for any possibilities.
Below will capture that infinite loop:
```python
while abs(guess**3 - cube) >= epsilon and guess <= cube:
```
___
## Bisection Search
The search checks if you are not close enough, is the guess *too big* or *too small*.\
if `g**2 > x` then we know g is too big.\
We know that the answer has to lie between `1` and `g`

Furthermore, if the new `g` is such that `g**2 < x`, then we know that it is too small. So\
we can keep finding the middle and continue with the search.

At each stage we are throwing away half the possible values. This is a significant jump in\
efficiency at guessing in this example.
___
### Square Root  example
```python
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low / 2.0)
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to quare root of ' + str(x))

```


We start with a search space from 0.0 up to 9. We know that the square root of 9 is 3, so we have an idea of where the\
algorithm will find the answer (this will help us through the explanation).
On each step, the algorithm determines if the answer is close enough to the answer we are looking for, within a margin\
of error (epsilon). If we square the answer (the middle point of the search space) and we get that its either larger or\
smaller than our initial number 9, it may still be the answer we are looking for if that difference is smaller than\
epsilon. (For example, if we say epsilon is 0.5, and we want the square root of 9, if our answer squared gives us 8.6\
or 9.4, those are "acceptable" answers because they are within that margin of error we've set, this is the meaning of\
epsilon)

If it's not within epsilon, it means it's not precise enough, and we have to reduce our search space even further.
But how do we determine where to keep looking? We can reduce our search space BY HALF on each step!

We can reduce our search space BY HALF! on each step by noting if the answer squared is too small or too large to be\
the right answer.
If our answer squared is too small, the algorithm will discard the half of the search space that contains numbers\
smaller than our answer, and our new search space will be the other half that contains numbers larger than our previous\
answer. Our new Low will be the previous answer (the middle point of the previous search space) and our High point\
will remain the same.

On the contrary, if our answer squared is too large to be the right answer, the algorithm will discard the HALF of the\
search space that contains numbers Larger than our previous answer. Our new High point will be the previous answer\
(the middle point of the previous search space) and our Low point will remain the same.

These steps will repeat until the algorithm finds an answer that, squared, is close enough to the initial number for\
which we are trying to calculate the square root. (in this case 9)

___
## Guess my number

Using a `while True` loop and bisection search we can narrow down guessing of a number significantly by removing\
half the possible solutions by asking if the answer is high or low.

The following guesses in increments is by dividing the guesses in half on the side which the user inputs as the guess\
being too high or too low. Then breaking it in half again and again until we find the guess which is correct.

```python
low = 0
high = 100
print("Please think of a number between 0 and 100")

while True:
    guess = int(high + low) //2 #this assigns the guess value to each iteration of high and low being divided by 2
    print("Is your secret number: " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. \
            Enter 'l' to indicate the guess is too low. \
            Enter 'c' to indicate I guessed correctly:")
            #assigning the input to a variable. In this instance 'ans'

    if ans == "c":
        print("Game over. Your secret number is " + str(guess))
        break
        #this is the break statement to get out of the loop once the input is 'c'
    elif ans == "h":
        high = guess
    elif ans == "l":
        low = guess
    else:
        print("Sorry, I did not understand your input")
        #else clause to catch any input that is not 'h', 'l' or 'c'.
        #it is still part of the while loop so WHILE TRUE it will keep putting them back to the beginning.
```



# Approximate Solutions
> When you want to get *close* to the answer but because there is an infinite number of possibilities, this is the\
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

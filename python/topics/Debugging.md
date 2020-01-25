#Debugging and setting yourself up
Programming can be difficult to debug if you go into it blindly so it is recommended to approach it with a formulaic\
perspective in order to break down your challenges and find the solution without putting yourself into a worse \
position.

**_Break the code up into modules_**\
It is easier to understand each module instead of dealing with run-on code and then trying to pinpoint the issue
The modules then are tested and debugged individually.

Additionally setting up the docstring to make sure we document what the input and expected output would be.

**_Set of Tests_**\
Unit Testing: Validate each piece of the program and test each function separately.\
Regression Testing: Catch and validate re-introduced errors that you fixed previously\
Integration Testing: Do no rush into integration testing. Complete the unit and regression testing first then\
when you come to integration testing, you can run the whole code.

**_Blackbox Testing_**\
Explores all the paths through the specifications of the code\
Blackbox testing never look at the code but only at the docstring or specs

**_Glassbox Testing_**\
Glassbox testing looks at the code and uses guidelines.
* Branches: exercises all parts of a conditional
* For loos: loop ot entered; only executed once?, More the once?
* While loops: same as for looks; cases that catch **all the exits**

### Overt and Covert Bugs

**_Overt Bugs_** are a obvious indication that something is wrong such as **code crashing**,\
**stops before the answer** or **infinite loops**

**_Covert Bugs_** are the non obvious bugs as they return *an* answer but it is difficult\
to initially see that the answer is incorrect.

### Persistent and Intermittent 
**_Persistent_** occurs every time such as the code *always crashes*
**_Intermittent_** is difficult as it only occurrs occasionally such as reliant on a web page or when time is a value

### Print Statement Debugging
Print statements are great for debugging, use the following steps to break it down:
* Print when you enter a function
* Print out the values of the parameter - Make sure they are what you expect.
* Print Result to check if its expected
* Bisection method used to debugging - Place the print statement in the middle of the code\
and work through and see if the bug is higher or lower.

### Error Messages
* Index Error - Trying to access something in a structure that is outside the length of that structure\
                e.g  test = [1, 2, 3,] then calling test[4]
* Type Error - Trying to convert an inappropriate type such as `int(test)`
* Name Error - References a non-existent variable
* Type Error - Mixing data types without appropriate coercion such as `'3' / 4`
* Syntax Error - Forgetting to close parenthesis, quotation etc such as `a = len([1, 2, 3]` then calling `print a`

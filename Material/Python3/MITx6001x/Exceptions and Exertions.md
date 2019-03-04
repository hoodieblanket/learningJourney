#Exceptions
Exceptions are used in order to tackle any exceptions or error that your code would otherwise generate. This is\
valuable as it means that you are in control of what your code does when it encounters a specific error or otherwise.

This could be exceptions for your own code running into issues or when you are calling on user input and it is not \
within the parameters of your code to execute i.e expecting a integer but user enters a string.

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("You have not put a valid number for your age")
```

This try clause will place the variable assignment and the user input inside a try clause to single out the potential\
of errors. If the user enters a integer then that number is assigned to the variable **age**.

If the user enters a string then it will encounter the ValueError. As previous errors just spat out a bunch of junk
\related to the ValueError and where to find it etc; this method actually captures that ValueError and then just \
proceeds to execute the code below the *except*.

The important thing for handling exceptions is that **_your program doesn't crash_**. Instead of the program finishing\
at the error, this actually handles the error and proceeds with the rest of your code.

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("You have not put a valid number for your age")
else:
    print("No exceptions were thrown")
print("The program continues to run")


```

The above changes the dynamic a little by using a else clause that boils down to; if there is no exceptions then run\
the following code and then proceed with the rest of the program as normal.

So with no exception:  it will print "No exceptions were thrown" and "The program continues ot run:"
With ValueError exception: it will print "You have not put a valid number for your age" and "the program continues..."

Furthermore you are able to identify errors as a variable and assigned to them.
##Assigning Exceptions to Variables
```python
try:
except ValueError as ex:
    age = int(input("Age: "))
    print("You have not put a valid number for your age")
    print(ex) # this will print the variable which has been assigned some memory of the ValueError produced
    print(type(ex)) # This will print the type of the exception that was thrown
else:
    print("No exceptions were thrown")
print("The program continues to run")


```
Repetitive code is bad practice because it may mean that if future changes need to be made, then you need to edit \
multiple lines in order to correct it all whereas if you aren't repeating your code, then the error or change just\
needs to occur to 1 piece of code.

The following is used if you want to capture more than 1 exception that is thrown and you want to use the same\
exception error message. Furthermore in the instance it captures a ZeroDivisionError.

It is important to note that if you had or have another `except` clause that was looking for ZeroDivisionError as well\
such as `except ZeroDivisionError: print("You have not put a valid number for your age")` then the code won't print\
out twice. It will only jump to the first except clause that the error hits then proceed to ignore the rest of the \
except clauses.

##Capturing Multiple Exceptions

```python
try:
    age = int(input("Age: ")) 
    xfactor = 10 / age # what if age is 0? This would no longer produce a ValueError
except (ValueError, ZeroDivisionError): # errors added in parenthesis and separated by comma
    print("You have not put a valid number for your age")
else:
    print("No exceptions were thrown")
print("The program continues to run")
```

The `finally` clause is always executed whether you have an exception or not. This is used to usually release resources\
such as closing files, data os connections, network connections and so on.

##Finally Clause
```python
try:
    file = open("app.py") # opening a file
    age = int(input("Age: ")) 
    xfactor = 10 / age # what if age is 0? This would no longer produce a ValueError
except (ValueError, ZeroDivisionError): # errors added in parenthesis and separated by comma
    print("You have not put a valid number for your age")
else:
    print("No exceptions were thrown")
finally:
    file.close() # closing down/release the resources being used

```
We do have a cleaner simple way that replaces the `finally` clause but it doesn't always work. It works with certain\
kinds of objects.

For example if you take the previous code and pay attention to the changes; we will use the With statement to\
accomplish the same thing.

##With Statement

```python
try:
    with open("app.py") as file: # using the with statement, the file object that the open function returns
        print("file opened") # whenever we open a file using with statement, python will automatically close\
        # the file without the need for a finally clause. with statement will auto free the resources
        
    age = int(input("Age: ")) 
    xfactor = 10 / age # what if age is 0? This would no longer produce a ValueError
except (ValueError, ZeroDivisionError): # errors added in parenthesis and separated by comma
    print("You have not put a valid number for your age")
else:
    print("No exceptions were thrown")
#finally:
 #   file.close() # closing down/release the resources being used
```

##Raising Exceptions

```python
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less") # raises the exception ValueError and prints out a statement
    return 10/age

try: #Instead of the program crashing with the error details, you can place the call inside a try block to control it
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

```
This is how you would raise an exception but it is not always recommended. Raising exceptions can be costly as it can\
affect other peoples codes. This takes the form of the time it takes to complete the code. For code that will only run\
once or so then it doesn't really effect the time that much however if you are programming for efficiency and \
scalability then a program that runs 10,000 times; previous code raising an exception actually takes 4x as long as the\
below code.

```python
def calculate_xfactor(age):
    if age <= 0:
        return None # none is an object that is absent of value
    return 10/age
    
xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass #

```

## Assertions
```python
def avg(grades):  
    assert not len(grades) = 0, 'no grades data'
    return sum(grades)/len(grades)
```

This would check if you made a mistake by giving an empty list. the assert statement will check if True/False if the
length of (grades) is 0. If it is not 0 then the `assert not ` statement will be true and then it will skip past.

However if it is False then it will proceed with the function

The Assert statement is not to control unexpected exceptions. It is to ensure the program halts if an expected exception\
is thrown. Usually this would be to check if inputs are valid or outputs of a function before returning the values.

The goal with assertions are to spot bugs as soon as they are introduced and make clear what happened.
We can use assertions as a supplement to your testing.


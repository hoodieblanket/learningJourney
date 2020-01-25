# Strings

Strings are immutable, meaning they cannot be modified and changed. We can certainly find the index of certain\
characters but the string cannot be interchanged or modified.\
You can redefine and change the variable but not the string.

For example S might equal `hello` and you might call on the [0] index to produce `h` however you cannot change the\
[0] index using methods such as `s[0] = "P"`. This courses an error as the *string* cannot be modified.

You can use methods to redefine it but it changes the variable. Such as assigning the variable to a new value\
`s = "p" + s[1:]` which will now produce `pello` however **s** is permanently redefined.



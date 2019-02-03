# FOR LOOPS RECAP

for loop can iterate over any set of values such as strings and not just numbers.\
For example if we produce the following code using the `len()` function:

```python
s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("there is an i or u")
```

Or a little cleaner:
```python
for char in s: 
    if char == 'i' or char == 'u':
        print("there is an i or u")
```

`in s` is called an iterable. It says that we can write a loop that starts with the first element of s, then the\
second element, then the third until it runs out of elements or characters in s in which case it will exit the\
loop.


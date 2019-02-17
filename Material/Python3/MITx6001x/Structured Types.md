# Tuples and Lists
A tuple is an ordered sequence of elements that can mix element types. Tuples are immutable, similar to strings,\
cannot change the values within the tuple; similar to strings.

tuples require the extra comma to indicate they are tuples. For example having just one tuple `t = ('one',)`: this\
will produce `('one',)`

Tuples are convenient for swapping variable values. Tuples allows you to swap variables without needing to use place\
holders such as `temp = x, x = y, y =  temp` if you wanted to switch the variables around. Tuples allows you to do \
it simply such as `(x,y) = (y,x)`

They are also used to return more than one value from a function. For example:

```python
quotient_and_remainder(x,y):
    q = x // y
    r = x % y
    return (q,r)
(quot,rem) = quotient_and_remainder(4,5)
```

The tricky part is going Tuples inside of Tuples. For example:
`dogsTuple = (("dog1", ("dog2",)), (("dog3",), ("dog4", "dog5")))`

In order to get to `dog1` we need to read what indices we are dealing with. `[0] = (("dog1", ("dog2",))` and
`[1] = (("dog3",), ("dog4", "dog5")))`

So using this info, to get to dog1 we need to access the first index [0]. The second layer of the list shows 'dog1'
being index [0]. This can be confirmed in shell when we use the follow `dogsTuple[0][0]` to access first list then 
get index [0].
 
However to get to dog2, it is inside another Tuple. So we need to access first list [0] then access second list [1]
then we can see we have a Tuple `("dog2",)` so dog2 is at the [0] index.


Tuples are iterable similar to the way strings are iterable.

#List
Ordered sequence of information accessible by index. We use square brackets to differentiate the list
The big difference with a list is that it is mutable: changeable values within the list.

Index can also be a variable or expression. It does not have to be a sole integer. We can assign a value to variable i\
and then when we use the `List[i-1]` it will equate to the variable minus the index @ [1]

#Operations on Lists
We can add more values to the *end* of list using the `.append(element)` method.
This has mutated the list. Any code that was relying on the List only being 3 elements long, is now in trouble as\
the list now has 4 elements.

Lists are Python objects, everything in Python is an object. Objects have data and with methods and functions we can \
access this information using object_name.do_something(). 

Lists can concatenate. List1 + List2 assigned to a new List3 will combine the Lists but not change the original lists.
.extend() can extend the list with the variables such as .extend([0,6]) will add 0 and 6 to a list.

We can use ` del(List[2])` to remove a item from the list *at a specific index*. Alternatively we can remove an element\
from the *end of the list* with the List.pop(), and returns the removed element. We can remove a *specific element* \
using the `List.remove(element)` method. This remove method will find a remove your element but if there is multiples\
then this will remove only the first occurrence. 

#Converting Lists to Strings and Back
We can convert a string to a list with `list(stringHere)` and this returns a list with every character from stringHere
We can use `stringHere.split()` to *split a string on a character* parameter. This splits on spaces if called without\
a parameter.

Can also use `''.join(L)` to turn a *list of characters into a string*, can give a character in quotes to add character\
between every element.

#Other List Operations
sort() will return a new version of it after mutating it. sorted() will provided a sorted version of the List but \
doesnt mutate it.\

`sorted(List)   :   will produce a sorted version without mutating the list`\
`List.sort()    :   will mutate the List into a sorted version`\
`List.reverse() :   will mutate the List into a reversed version`\


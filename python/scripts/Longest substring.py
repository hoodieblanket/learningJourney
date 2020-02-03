s = 'cnpazcboboaos'

current = ""
last = ""
longest = ""

for i in s:
    if  last <= i:
       current += i
       if len(current) > len(longest):
           longest = current
    else:
        current = i
    last = i

#for every value in the variable *s*
#   if the *last* string is less than or equal to the value *i*
#       then append the *i* value to the *current* string
#       if the length(size) of the *current* string is greater than the length(size) of the *longest* string
#           then the *longest* string copies and becomes the *current* string which is larger.
#   or else if not less than or equal; then *current* string resets and becomes just the value of *i* at this time
#   also *last* is reset as well so that we can compare future *i* values to see if *i* is greater than the value of *last* and this will determine whether we continue to add more values to the *current* variable or if we reached a limit for the longest string we went in alphabetical order.
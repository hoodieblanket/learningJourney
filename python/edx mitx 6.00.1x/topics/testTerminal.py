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

#Looking for repeats or specific arrangements in a string
s = 'azcbobobegghakl'

total = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        total +=1

print("Number of times bob occurs is: " + str(total))
# fibonacci numbers and using a dictionary

def fib_efficient (n,d):
    # n being the number we want to computer and d being the dictionary that we have developed
    if n in d:
        return d[n]
        # if statement checks if we have already stored the answer in dictionary then returns the answer instead of computing it
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

#test case
d = {0:0, 1:1}
print(fib_efficient(12, d))

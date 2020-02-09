#fibonacci problem and solution
# after one month (0) - 1 female
# after two month - still 1 female (now preggo)
# after thrid month - two females, one preggo, one not
# in gemeran, females(n) = females (n-1) + females (n-2)
#every female alive at month n-2 will produce one female in a month n
#these can be added to those alive in month n-1 to get total alive in month n

# you have two base cases
# 1) females (0) = 1
# 2) females (1) = 1
#recursive case
# females(n) = females(n-1) + females (n-2)

def fib(x):
    if x == 0 or x == 1:
        return 1
    #both base cases checked!
    else:
        return fib(x-1) + fib(x-2)

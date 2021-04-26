def polysum (n,s):
    """
    n = integer, representing the number of sides
    s = integer, the length of the side
    """
    import math
    sum_of_area = (0.25*(n))*(s**2)/math.tan(math.pi/n)
    perim = n*s
    ans = sum_of_area + perim**2
    return round(ans,4)
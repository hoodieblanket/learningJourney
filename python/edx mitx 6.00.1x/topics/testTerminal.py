def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    for i in aDict:
        # 'a'
        if len(i) == 0:
            return None
        elif aDict[i] >= max(aDict.values()):
            return i

biggest({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0], 'c': [1, 2, 3, 4]})
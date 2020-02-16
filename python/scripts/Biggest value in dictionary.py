def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    for i in aDict:
        if len(i) == 0:
            return None
            # capture any empty values in dict
        elif aDict[i] >= max(aDict.values()):
            # need to force *max* to take max of values rather then max of keys. If you do not append the mod .values() then it will take the last key as the max. i.e 'D' is last and 'A' is first
            return i

#test dictionary
biggest({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0], 'c': [1, 2, 3, 4]})
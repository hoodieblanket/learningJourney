def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = aTup[0::2]
    return newTup

aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))
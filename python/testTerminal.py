class intSet:
    """ An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once"""

    def __init__(self):
        """create an empty set of integers"""
        self.vals = []
    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        """Asumes e is an integer
        Returns true if e is in self, and false otherwise"""
        return e in self.vals
    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + " not found")
    def __str__(self):
        """returns a string representation of self"""
        self.vals.sort()
        result = ""
        for e in self.vals:
            result = result + str(e) + ","
        return "{" + result[:-1] + "}"

s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(6)
s.remove(3)
s.insert(6)
print(s)
s.remove(3)

>>> s = intSet()
>>> print(s)
{}
>>> s.insert(3)
>>> s.insert(4)
>>> s.insert(3)
>>> print(s)
{3,4}
>>> s.member(3)
True
>>> s.member(6)
False
>>> s.remove(3)
>>> s.insert(6)
>>> print(s)
{4,6}
>>> s.remove(3)
ValueError: 3 not found
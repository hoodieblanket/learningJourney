#Classes
Classes are a blueprint of creating new objects similar to how int, float and boolean are objects.\
Objects are an instance of class. The difference would be as such `Class = Human` whereas `Object = Mary, Johan, Sue`\

When using the dot notation with a list object = [], then we utilize *methods* `object.method` to interact with the\
list. such as object.add() or object.remove() etc or object.get_total()

```python
class Point:
    def draw(self):
        print("draw")
        
point = Point() # now we can call the Point class and assign it to the point variable
print(type(point)) #if we asked what type point would be, it would show __main__.Point. as we created our own object.
point(isinstance(point, Point)) # Boolean True would return as point is an instance of the Point object.
point(isinstance(point, int)) # Boolean False would return as point is not an instance of the class int

```

#Constructor
__init__(self) is called a magic method and it is a constructor. self is a reference to the current Point object.

A constructor is created or used when you first create a new point object.

```python
class Point:
    def __init__(self, x, y): # all methods we define in a class need atleast 1 parameter. which is conventionally self\
        self.x = x or 0
        self.y = y
        

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1,2)
#now when you use the .operator then the x and y are methods

point.draw() # this will print the draw function

```
Self is a reference to the current point object
self - To explain self, as per above, when we call on the point class, python will internally create the point object\
in memory and set self to reference that point object.\
This point object has a bunch of methods we have used before (methods like upper, lower, sort etc) but can also be assigned\
attributes as a method. An example above is assigned x and y variables are methods


For example a Human class can have attributes like height, weight and colour but also functions like walk, talk and so on\

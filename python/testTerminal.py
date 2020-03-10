class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self): 
    #as mentioned with methods inside the class, the first argument will always be the instance, `self` and we only need `self` in order to get the full name
        return "{} {}".format(self.first, self.last)

emp_1 = Employee('Johann', 'Van Niekerk', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.fullname) 
# This will only print and confirm that `fullname` is indeed a method.
# So as we do with methods we need to have parenthesis to call the method
print(emp_1.fullname())
print(emp_2.fullname())

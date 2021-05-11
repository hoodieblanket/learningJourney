class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # these are all attributes of our class
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"


employee_1 = Employee("Super", "Star", 50000)
# the instance is created automatically so you don't need to provide an argument for 'self'
# employee_1 being passed in, automatically creates the instance and then assigns all 'self' to equal employee_1.
# #i.e employee_1.first or employee_1.email etc..
employee_2 = Employee("Bundy", "Coke", 60000)

print(employee_1.email)
print(employee_2.pay)

print(employee_1.fullname())
print(employee_2.fullname())

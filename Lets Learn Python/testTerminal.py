course = "Python Programming"
# Does not effect the original variable or change it
print(course.upper())  # Outputs uppercase
print(course.lower())  # Outputs lower case
# assign a variable with the course variable amended with the UPPER method
course_upper = course.upper()
print(course_upper)  # Outputs the new variable
print(course)  # Shows the original variable is not effected
print(course.title())  # Outputs in Title, first letter uppercase
# Outputs variable and strips the while space at the front and back of a string
print(course.strip())
print(course.rstrip())  # Strips white space on right of variable/end of a string
print(course.lstrip())  # Strips white space on left
# this is valuable for any variables which requires user input so you can remove any white space
# Finds the index or a character or series of characters
print(course.find("Pro"))
# Python is case sensitive, so this would show string is not found
print(course.find("pro"))
print(course.replace("P", "j"))
print("pro" in course)
print("Pro" in course)  # an expression that returns a boolean
print("swift" not in course)  # an expression that returns a boolean

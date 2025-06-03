class Employee:
    # name = "Abhinav"
    language = "Python" # This is a class attribute
    salary = 12000

Abhinav = Employee()
Abhinav.name = "Abhinav Lather"
Abhinav.language = "Java" # This will override the class attribute and is known as instance attribute
print(Abhinav.name, Abhinav.language, Abhinav.salary)

# name is object attribute and salary and language are class attributes.

 
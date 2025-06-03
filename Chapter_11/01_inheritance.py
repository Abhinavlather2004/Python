class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    # def show(self):
    #     print(f"The name is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

# Creating an Employee object
a = Employee()
a.name = "Alice"
a.salary = 50000

# Creating a Programmer object
b = Programmer()
b.name = "Bob"
b.salary = 80000
b.language = "Python"

# Accessing company variables
print("Employee company:", a.company)
print("Programmer company:", b.company)

# Using methods
a.show()             # From Employee
b.show()             
b.showLanguage()     # Specific to Programmer

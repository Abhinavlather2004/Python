class Employee:
    language = "Python"
    salary = 12000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

Abhinav = Employee()
Abhinav.language = "Java"  # This will override the class attribute and is known as instance attribute
Abhinav.getInfo()
Abhinav.greet()
# Employee.getInfo()

#If made staticmethod, it can be called without self
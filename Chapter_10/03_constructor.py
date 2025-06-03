class Employee:
    language = "Python"
    salary = 12000

   
    def __init__(self, name, salary, language):  # dunder method which is automatically called when an object is created
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

Abhinav = Employee("Abhinav Lather", 12000, "C++")
# Abhinav.name = "Abhinav Lather"
print(Abhinav.name, Abhinav.salary, Abhinav.language)  
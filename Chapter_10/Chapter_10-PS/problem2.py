class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")
    def squareroot(self):
        print(f"The square root of {self.n} is {self.n ** 0.5}")
    @staticmethod
    def greet():
        print("Hello, welcome to the Calculator program!")

a = Calculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()
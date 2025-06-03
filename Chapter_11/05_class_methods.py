class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()

#if we declare class method then it will give class attribute not instance attribute.


# class Employee:
#     a = 1
#     # @classmethod
#     def show(self):
#         print(f"The class attribute of a is {self.a}")

# e = Employee()
# e.a = 45
# e.show()
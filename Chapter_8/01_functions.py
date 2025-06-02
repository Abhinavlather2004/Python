# Manually calculate the average of three numbers
# a = 12
# b = 43
# c = 54
# average = (a + b + c) / 3
# print(average)

# Functioan definition

def avg():
    """Calculate the average of three numbers."""
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    average = (a + b + c) / 3
    print(average)

# Function call
avg()
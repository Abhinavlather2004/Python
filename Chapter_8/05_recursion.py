n = int(input("Enter a number to calculate its factorial: "))
def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(n)
print(f"The factorial of {n} is {result}.")
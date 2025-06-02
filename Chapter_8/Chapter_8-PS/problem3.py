n = int(input("Enter a number to find sum upto it: "))

def sum_upto(n):
    # if n < 0:
    #     return 0
    # elif n == 0:
    #     return 0
    if n == 1:
        return 1
    else:
        return n + sum_upto(n - 1)
    
print(sum_upto(n))
# result = sum_upto(n)
# print(f"The sum of all numbers from 1 to {n} is: {result}.")
# list comprehension to create a multiplication table
n = int(input("Enter a number: "))

table = [n * i for i in range(1, 11)]
print(table)


# n = int(input("Enter a number: "))

# table = [n * i for i in range(1, 11)]
# with open("tables.txt", "a") as f:
#     f.write(str(table) + "\n")
#     f.write(f"Table of {n}: {str(table)}\n")

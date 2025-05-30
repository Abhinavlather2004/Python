# for i in range(1, 11):
#     print(i*5)
     

n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}")


i = 1
while (i<=10):
    print(f"{n} * {i} = {n * i}")
    i += 1

for i in range(1, 11):
    print(f"{n} * {11-i} = {n * (11-i)}")
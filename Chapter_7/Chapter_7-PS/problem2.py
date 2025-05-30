n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number")
        # print("number is not prime)")
        break
else:       
    print(f"{n} is a prime number")
    # print("number is prime)")

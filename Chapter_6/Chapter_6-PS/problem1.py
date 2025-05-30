a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a > b and a > c and a > d):
    print("Greatest number is:", a)
elif(b > a and b > c and b > d):
    print("Greatest number is:", b)
elif(c > a and c > b and c > d):
    print("Greatest number is:", c)
elif(d > a and d > b and d > c):
    print("Greatest number is:", d)
else:
    print("There is no largest number, they are all equal or invalid input.")

a = int(input("Enter your age: "))

# Multiple if statements with independent conditions with ladder logic
if(a%2==0):
    print("You are an even age.")

# If elif else ladder
if(a > 18):
    print("You are an adult.")
elif(a == 18):
    print("You are just an adult.")  
else:
    print("You are a minor.")

print("End of program")


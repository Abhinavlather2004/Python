for i in range(20):
    if(i==10):
        print("Breaking at 10")
        break
    print(i)


for i in range(20):
    if(i==10):
        print("Skipping 10")
        continue
    print(i)


# Pass statement is used when you need a statement syntactically but do not want to execute any code. 
# Skipping for now
for i in range(20):
    if(i==10):
        pass  # Do nothing
    print(i)
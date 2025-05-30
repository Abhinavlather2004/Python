marks1 = int(input("Enter marks of first subject: "))
marks2 = int(input("Enter marks of second subject: "))
marks3 = int(input("Enter marks of third subject: "))

total_percentage = (100 * (marks1 + marks2 + marks3)) / 300

if(total_percentage > 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are pass with percentage: ", total_percentage)
else:
    print("You are fail with percentage: ", total_percentage)   
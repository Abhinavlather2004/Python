import os
#specify the directory you want to list
directory_path= '/Users/abhinavlather'

#list the contents of the directory
contents = os.listdir(directory_path)

# Print the contents of the directory
for item in contents:
    print(item)

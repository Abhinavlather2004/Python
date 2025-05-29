#String is immutable, cant be changed
name = "ABHinav"

# To access a character in a string, we can use indexing
print(name[0])  # Output: A

# To get the length of a string, we can use the len() function
print(len(name))  # Output: 7

print(name.endswith("av"))  # Output: True
# To check if a string starts with a certain substring, we can use the startswith() method

print(name.startswith("Abhi"))  # Output: False
# To check if a string contains a certain substring, we can use the in operator

print("hi" in name)  # Output: False

# To capitalize the first letter of a string, we can use the capitalize() method
print(name.capitalize())  # Output: Abhinav

# To convert a string to uppercase, we can use the upper() method
print(name.upper())  # Output: ABHINAV

# To convert a string to lowercase, we can use the lower() method
print(name.lower())  # Output: abhinav

# To concatenate strings, we can use the + operator
greeting = "Hello, " + name
print(greeting)  # Output: Hello, ABHinav

# To get a substring, we can use slicing
nameshort = name[0:4]
#if first index is not given, it will start from 0
#if last index is not given, it will go till the end
nameshort1 = name[-7:-3]
print(nameshort)
print(nameshort1)  # Output: ABHi




# Escape sequence characters:

# \n is used to create a new line in a string
# \t is used to create a tab in a string
# \\ is used to create a backslash in a string
# \' is used to create a single quote in a string
# \" is used to create a double quote in a string
a = "Hello\nWorld"
b = "Hello\tWorld"
c = "Hello\\World"
d = "Hello\'World"
e = "Hello\"World"
print(a)  # Output: Hello
           #         World
print(b)  # Output: Hello    World
print(c)  # Output: Hello\World
print(d)  # Output: Hello'World
print(e)  # Output: Hello"World

name.find("  ")  # Output: -1 (not found) #double space not found


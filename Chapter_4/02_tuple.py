# A tuple is immutable, meaning it cannot be changed after creation.
# Tuples are defined using parentheses ().
# Tuples can contain elements of different data types, including other tuples.

a = (1, ) # A single element tuple must have a comma after the element
print(type(a)) 
# a[0] = 3 # This will raise a TypeError because tuples are immutable


# Tuple methods:

b = (1, 2, 3, 4, 5)
print(b.count(2))  # Counts the number of occurrences of 2 in the tuple
print(b.index(3))  # Returns the index of the first occurrence of 3 in the tuple

# Tuple unpacking
c = (10, 20, 30)
x, y, z = c
print(x, y, z)  # Output: 10 20 30

# Nested tuples
d = (1, (2, 3), 4)
print(d[1])  # Output: (2, 3)

# Accessing elements in a tuple
print(d[1][0])  # Output: 2 (accessing the first element of the nested tuple)

# Concatenation and repetition
e = (1, 2) + (3, 4)  # Concatenation

f = (5, 6) * 2  # Repetition

print(e)  # Output: (1, 2, 3, 4)
print(f)  # Output: (5, 6, 5, 6)

# Length of a tuple
print(len(b))  # Output: 5 (length of the tuple b)

# Checking if an element exists in a tuple
print(3 in b)  # Output: True (3 is in the tuple b)
 
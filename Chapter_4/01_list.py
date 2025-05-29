# Lists are containers to store a set of values of any data type.
# Lists are mutable, meaning they can be changed after creation.
# Lists are defined using square brackets [].
# Lists can contain elements of different data types, including other lists.

# Example of a list
list = [1, 2, 3, "Hello", 4.5, True]

# Accessing elements in a list using indexing
print(list[0])  # Output: 1
print(list[3])  # Output: Hello

# Getting the length of a list using len() function
print(len(list))  # Output: 6

# Checking if an element is in a list using the in operator
print(2 in list)  # Output: True
print("Hello" in list)  # Output: True

list.append(6)  # Adding an element to the end of the list
print(list)  # Output: [1, 2, 3, 'Hello', 4.5, True, 6]

list.remove(2)  # Removing an element from the list
print(list)  # Output: [1, 3, 'Hello', 4.5, True, 6]

list.insert(1, "World")  # Inserting an element at a specific index
print(list)  # Output: [1, 'World', 3, 'Hello', 4.5, True, 6]


# list.sort()  # Sorting the list in ascending order
# Note: Sorting will raise an error if the list contains mixed data types



l1 = [1, 2, 7, 5, 3]
l1.sort()  # Sorting the list in ascending order
print(l1)  # Output: [1, 2, 3, 5, 7]

# Reversing the list
l1.reverse()  # Reversing the list
print(l1)  # Output: [7, 5, 3, 2, 1]

l1.pop()  # Removing the last element from the list
print(l1)  # Output: [7, 5, 3, 2]

l1.pop(3)  # Removing the element at index 3
print(l1)  # Output: [7, 5, 3]

l1.clear()  # Clearing the list
print(l1)  # Output: []

# If we perform an operation on a list and print it, it will show the updated list.
# And further the next operation performs on the updated list.
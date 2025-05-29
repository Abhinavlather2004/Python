# It is unordered
# It is mutable
# It is indexed by keys
# It is a collection of key-value pairs
# It is defined using curly braces {}
# It can contain mixed data types
# It can contain duplicate values but not duplicate keys

marks = {
    "Abhinav": 100,
    "Shubham": 56,
    "Rohan": 23
}

print(marks.items())
print(marks.keys()) 
print(marks.values())
marks.update({"Abhinav": 99, "Shubham": 100})
print(marks)
print(marks["Abhinav"])
print(marks["Abhinav"], type(marks["Abhinav"]))  
print(marks, type(marks))
print(marks.get("Abhi")) # This will return None if "Abhi" is not found
# print(marks.get["Abhi"]) # This will raise an error because get is a method, not a dictionary key

d = {} # This is an empty dictionary
d = dict() # This is also an empty dictionary

print(len(marks))  # Length of the dictionary
# Set is a collection of unique elements.
# It is unordered
# It is unindexed
# It is mutable

e = set() #Dont use s={} as it is a empty dictionary

f= {1, 5, 56, 2, 5, 5, 7, 23, 65} # Set will print unique elements without any order
# print(f) # {1, 2, 5, 7, 23, 56, 65}


s = {1, 5, 23, 5, 6, 7, 34, 23, "Abhinav"}

print(s, type(s))  
 
s.add(100) # Add an element to the set
print(s)  # {1, 2, 5, 6, 7, 23, 34, 'Abhinav', 100}

s.remove(100)  # Remove an element from the set
print(s)  # {1, 2, 5, 6, 7, 23, 34, 'Abhinav'}

s.discard(100)  # Discard an element from the set, does not raise error if element is not present
print(s)  # {1, 2, 5, 6, 7, 23, 34, 'Abhinav'}

s.pop()  # Remove and return an arbitrary/random element from the set  
print(s)  # {2, 5, 6, 7, 23, 34, 'Abhinav'} (the first element is removed)

s.pop()
print(s)

# For union: example:
#print(s1.union(s2))
# For intersection: example:
#print(s1.intersection(s2))
# For subset: example:
#print(s1.issubset(s2))



''' Instructions for practice exercise 5.5
 Write a Python program to merge two dictionaries into one.'''

# Define two dictionaries
dict1 = {
    "Tuples": "A collection of objects seperated by commas.",
    "Dictionary": "A collection of key-value pairs.",
}
dict2 = {
    "Strings": "A collection of characters.",
    "Variables": "Containers for storing values."
}

# Merge through the | operator and display the output
print(dict1 | dict2)
''' Instructions for practice exercise 5.2
Write a Python program to iterate through the keys of a dictionary and print them'''

# Stores key-value pairs of a dictionary
my_dict = {
    "Name": "Joshua Gofulco",
    "Age": 17,
    "Residence": "Abu Dhabi",
}

# Goes through the keys and displays them
for key in my_dict.keys():
    print(key)

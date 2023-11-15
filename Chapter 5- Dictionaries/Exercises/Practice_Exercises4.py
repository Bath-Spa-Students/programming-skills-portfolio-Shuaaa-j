''' Instructions for practice exercise 5.4
Write a Python program to iterate through both the keys 
and values of a dictionary and print them '''

# Stores key-value pairs in the dictionary
my_dict = {
    "Name": "Joshua Gofulco",
    "Age": 17,
    "Residence": "Abu Dhabi",
}

# Iterate through both keys and values and print them
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

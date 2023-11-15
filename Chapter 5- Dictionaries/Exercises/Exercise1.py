''' Instructions for exercise 5.1
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.'''

# Stores key-value pairs of personal information
info = {
    "first": "Eden",
    "last": "Gofulco",
    "age": 52,
    "city": "Abu Dhabi"
}

# Printing key-value pairs stored in the dictionary
print("First Name:", info["first"])
print("Last Name:", info["last"])
print("Age:", info["age"])
print("City:", info["city"])

print("Dictionary items:", info.items())


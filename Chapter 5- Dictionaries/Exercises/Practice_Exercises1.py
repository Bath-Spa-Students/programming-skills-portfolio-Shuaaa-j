''' Instructions for practice exercise 5.1
Use a dictionary to store information about yourself '''

# Stores key-value pairs of personal information
info = {
    "Name": "Joshua Gofulco",
    "Age": 17,
    "Residence": "Abu Dhabi",
    "Hobbies": ["Reading", "Chess", "Boxing"],
}

# Access and displays the personal information
print("Name:", info["Name"])
print("Age:", info["Age"])
print("Residence:", info["Residence"])
print("Hobbies:", ', '.join(info["Hobbies"]))


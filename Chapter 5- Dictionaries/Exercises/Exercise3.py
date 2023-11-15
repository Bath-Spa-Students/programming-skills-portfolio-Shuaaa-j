''' Instructions for exercise 5.3
Now that you know how to loop through a dictionary,
clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. 
When you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should automatically be included in the output.'''

# Defines the initial glossary
glossary = {
    "Strings": "A collection of alphabetical characters.",
    "Variables": "Containers for storing values.",
    "Tuples": "A collection of objects seperated by commas.",
    "Dictionary": "A collection of key-value pairs.",
    "Lists": "A collection of items that can contain various data types."
}

# Adds new terms to the glossary.
glossary["Float"] = "Float contains decimals and integers. "
glossary["Integer"] = "is a whole number without decimals."
glossary["Value"] = "An item associated with a key."
glossary["Comments"] = "A note in a program meant to help humans and starts with a #."
glossary["Boolean Expressoion"] = "An expression that evaluates to True or False."

# Printing the glossary using a loop with a newline 
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")





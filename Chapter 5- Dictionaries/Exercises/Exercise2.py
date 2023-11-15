''' Instructions for exercise 5.2
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
* Think of five programming words you’ve learned about in the previous chapters.
Use these words as the keys in your glossary, and store their meanings as values.
* Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

# Defines a glossary using a dictionary
glossary = {
    "String": "A collection of alphabetical characters.",
    "Variable": "Containers for storing values.",
    "Tuple": "A collection of objects seperated by commas.",
    "Dictionary": "A collection of key-value pairs.",
    "List": "A collection of items that can contain various data types."
}

# Access and prints the definition of the words
words = "String"
print("\n" + words + ": " + glossary[words])

words = "Variable"
print("\n" + words + ": " + glossary[words])

words = "Tuple"
print("\n" + words + ": " + glossary[words])

words = "Dictionary"
print("\n" + words + ": " + glossary[words])

words = "List"
print("\n" + words + ": " + glossary[words])


''' Instructions for exercise 2.3
Tidy up the code to make it easier to understand
Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, “\t” and “\n”, at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().'''

# Assigns a value to the variable 'name'
name = "\tJoshua Gofulco\n"

# Prints the name with whitespace 
print("\nName with whitespace:", name)  

# Prints the name using lstrip()
print("\nName with the lstrip() function:", name.lstrip())

# Prints the name using rstrip()
print("\nName with the rstrip() funtion:", name.rstrip())

# Prints the name using strip()
print("\nName with the strip():", name.strip())
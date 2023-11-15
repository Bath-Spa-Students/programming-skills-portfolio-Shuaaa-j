''' Instructions for exercise 7.3
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.'''

# Declaring a function
def make_shirt(size, message):
    print(f"A {size}-sized shirt with the message print of '{message}'")

# Using positional arguments
make_shirt("XXL", "Functions are cool!")

# Using keyword arguments
make_shirt(size="medium", message="Why do python programmers prefer eating Subway sandwiches? Because they’re great at handling strings!")




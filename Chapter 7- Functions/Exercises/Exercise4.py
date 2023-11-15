''' Instructions for exercise 7.4
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

# Declaring a function
def make_shirt(size="large", message="I love Python"):
    print(f"A {size}-sized shirt with the message print of '{message}'")

# Default 
make_shirt()

# Creates a medium shirt with the default message using the function
make_shirt(size="medium")

# Creates a small shirt with a custom message using the function
make_shirt("small", "Lambda functions are so confusing!")




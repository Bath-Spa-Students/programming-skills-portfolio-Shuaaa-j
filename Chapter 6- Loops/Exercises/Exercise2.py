''' Instructions for exercise 6.2
A movie theater charges different ticket prices depending on a person’s age.
If a person is under the age of 3, the ticket is free;
if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket'''

# Assigns values to the variables to be asked
question = "Good day! How old are you?"
question += "\nEnter 'done' when you finish buying tickets. "

# Creates an infinite loop until the user inputs 'done'
while True:
    age = input(question) # Asks input from user
    if age == 'done': # Checks if the user wants to exit the loop
        print("Thank you so much!")
        break

    age = int(age) # Converts the input to integer

    # Checks the age range and prints the corresponding prices
    if age < 3:
        print("  The ticket is free! Anything else?")
    elif age >= 3 and age < 13:
        print("  The ticket costs $10. Anything else?")
    else:
        print("  The ticket costs $15. Anything else?")

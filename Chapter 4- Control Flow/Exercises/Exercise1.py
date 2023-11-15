''' Instructions for Exercise 4.1
Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)'''

# Assigning a value to the variable
alien_color = "green"

# Check if the alien color is green
if alien_color == "green":
    # If true, print a message congratulating the player on earning 5 points
    print("Congratulations! You just earned 5 points.")

# Assigning a value to the variable
alien_color = "red" 

if alien_color == "green":
    # No output as the condition wasn't met
    print("Congratulations! You just earned 5 points.")
''' Instructions for exercise 4.2
Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
•If the alien’s color isn’t green, print a sta
tement that the player just earned 10 points.
•Write one version of this program that runs the if block and another that runs the else block.'''

# Assigning a value to the variable
alien_color = "green"

# If the condition is met, print the if block, else print the else block
if alien_color == "green":
    # Print a message indicating that the player earned 5 points for shooting a green alien
    print("You just earned 5 points for shooting a green alien!")
else:
    # Print a message indicating that the player earned 10 points for shooting an alien that isn't green
    print("You just earned 10 points for shooting an alien that isn't green!")

alien_color = "yellow" 

if alien_color == "green":
    print("You just earned 5 points for shooting a green alien!")
else:
    print("You just earned 10 points for shooting an alien that isn't green!")



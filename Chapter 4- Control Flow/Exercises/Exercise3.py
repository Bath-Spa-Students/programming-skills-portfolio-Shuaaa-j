''' Instructions for exercise 4.3
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
•	 If the alien is green, print a message that the player earned 5 points.
•	 If the alien is yellow, print a message that the player earned 10 points.
•	 If the alien is red, print a message that the player earned 15 points.
•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.'''

# Assigning a value to the variable
alien_color = "green"

# # If the condition is met, print the if block, else print the elif or else block
if alien_color == "green":
    print("You just earned 5 points for shooting a green alien.")
elif alien_color == "yellow":
    print("You just earned 10 points for shooting a yellow alien.")
else:
    print("You just earned 15 points for shooting a red alien.")

alien_color = "yellow"

if alien_color == "green":
    print("You just earned 5 points for shooting a green alien.")
elif alien_color == "yellow":
    print("You just earned 10 points for shooting a yellow alien.")
else:
    print("You just earned 15 points for shooting a red alien.")

alien_color = "red"

if alien_color == "green":
    print("You just earned 5 points for shooting a green alien.")
elif alien_color == "yellow":
    print("You just earned 10 points for shooting a yellow alien.")
else:
    print("You just earned 15 points for shooting a red alien.")


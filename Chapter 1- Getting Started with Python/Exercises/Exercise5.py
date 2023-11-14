''' Instructions for exercise 1.5
Write a Python program which accepts the radius of a circle from the user and compute the area.'''

# Assign the value of pi
pi = 3.14

# Get the radius of the circle from the user and convert it to a float
r = float(input ("Input the radius of the circle : "))

# Calculate the area of the circle using the formula and convert it to a string to display
Calculate_Area = str(pi * r**2)

# Print the result
print ("The area of the circle with radius " + str(r) + " is: " + Calculate_Area)

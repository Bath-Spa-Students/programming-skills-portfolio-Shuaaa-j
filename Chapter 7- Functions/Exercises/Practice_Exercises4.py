''' Instructions for practice exercise 7.4
Write a Python program that defines a function to calculate the area of a circle, and then
calls that function with a given radius.'''

pi = 3.14

# This function calculates the area of a circle.
def calculate_circle_area(radius):
    area = pi * (radius ** 2)
    return area

# Inputs the radius from the user
radius = float(input("Input the radius of the circle: "))

# Calculate the area and display the result using the function
area = calculate_circle_area(radius)
print(f"The area of a circle with the radius of {radius} is {area:.2f}")

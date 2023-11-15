''' Instructions for practice exercise 6.3
Write a Python program that uses a loop to find the sum of all the numbers from 1 to 100.'''

# variable to store the sum
total = 0 

# Uses the for loop and range attribute to go from 1 to 100
for num in range(1, 101):
    total += num  # Adds each number from 1 to 100 to the total

print(total, "is the sum of numbers from 1 to 100" )

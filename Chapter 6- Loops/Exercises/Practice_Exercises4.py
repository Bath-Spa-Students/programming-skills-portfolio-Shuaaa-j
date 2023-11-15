''' Instructions for practice exercise 6.4
Write a Python program that uses the break statement to exit a for loop when a specific
condition is met.'''

# Assigning a value to a variable
target = 5

# Uses the for loop and range attribute to go from 1 to 10 and meet the condition
for num in range(1, 11):
    if num == target:
        print(f"The target value '{target}' is found.")
        break
    print(f"Number: {num}")

print("Loop has ended.")

''' Instructions for practice exercise 6.5
Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop.'''

nums = []

# Use a while loop to continuously get user input
while True:
    # GetS user input
    num = input("Enter a number or press '0' to exit: ")

    # Check if the input is '0' to exit the loop
    if num == "0":
        break

    try:
        #converts the input to a float
        fnum = float(num)

    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input")
        continue

    # Append the valid number to the list 'nums'
    nums.append(fnum)

# Finds the largest number in the list
largest = max(nums)

# Prints the largest number
print("Largest number is", largest)


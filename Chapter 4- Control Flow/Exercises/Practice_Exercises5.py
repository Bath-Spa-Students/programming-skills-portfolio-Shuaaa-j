''' Instructions for practice exercise 4.5
Write a Python program that uses the elif statement to determine
the season based on the month provided as input.'''

# Asks for the input and converts it an integer
month = int(input("Enter the month (1-12): "))


# Declaring the if-else condition to determine the season based on the month
if 1 <= month <= 2 or month == 12:
    season = "Winter"
elif 3 <= month <= 5:
    season = "Spring"
elif 6 <= month <= 8:
    season = "Summer"
elif 9 <= month <= 11:
    season = "Autumn"
else:
    season = "Invalid input (Month should be between 1 and 12)"

# Displays a string and the result
print("The season for the given month is:", season)

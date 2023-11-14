''' Instructions for exercise 2.5
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
You will to use the arithmetic operators to complete this exercise.'''

# Defines the cost of each USB stick and the total budget
usb_cost = 6  
money = 50  

# Calculates the maximum number of USB sticks she can buy
usb_bought = money // usb_cost

# Calculates the amount of money left after buying USB sticks
remaining_money = money % usb_cost

# Prints the results
print(f"With £{money}, the girl can buy {usb_bought} USB sticks and have £{remaining_money} left.") 



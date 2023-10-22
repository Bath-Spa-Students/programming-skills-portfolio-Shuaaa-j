''' Instructions for exercise 2.1
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.'''


usb_cost = 6  
money = 50  

usb_bought = money // usb_cost
remaining_money = money % usb_cost

print("The girl can buy", usb_bought, "USB sticks, and have £", remaining_money, "left.")


''' Instructions for exercise 6.5
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches.'''

# List of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = [ 
    "Egg", "Spam", "Cheese", "Pastrami", 
    "Steak", "Pastrami", "Chicken", "Pastrami"]

# List for finished sandwiches
finished_sandwiches = []

print("I'm sorry, we've seem to run out of pastrami today.")
while "Pastrami" in sandwich_orders: # Removing "Pastrami" from the list of sandwich orders 
    sandwich_orders.remove("Pastrami")

# Loops through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first order
    print(f"I'm currently making your {current_order} sandwich.")
    finished_sandwiches.append(current_order) # Adds the finished sandwich to the end of the list

# Prints the list of finished sandwiches
print("\nOrder up for the following sandwiches:")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich.")

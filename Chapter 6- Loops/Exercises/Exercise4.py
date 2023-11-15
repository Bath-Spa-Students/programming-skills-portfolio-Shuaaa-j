''' Instructions for exercise 6.4
Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made.'''

# Creates the list of  orders
sandwich_orders = ["Egg", "Spam", "Cheese", "Steak"]

# List for finished sandwiches
finished_sandwiches = []

# Loops through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first order
    print(f"I'm currently making your {current_order} sandwich.")
    finished_sandwiches.append(current_order) # Adds the finished sandwich to the end of the list

# Prints the list of finished sandwiches
print("\nOrder up for the following sandwiches:")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich.")

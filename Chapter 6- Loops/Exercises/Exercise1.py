''' Instructions for exercise 6.1
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
As they enter each topping, print a message saying you’ll add that topping to their pizza.'''

# Empty list to store toppings
p_toppings = []  

while True:
    topping = input("Enter a pizza topping (or type 'end' to finish): ")
   
    if topping == "end" :
        break  # Exits the loop if the user enters 'end'
   
    print(f"{topping} has been added to your pizza.")
    p_toppings.append(topping) # Adds it to the end of the list

# Prints the final list of selected pizza toppings
if p_toppings:
    print("\nThe pizza will have the following toppings:")
    for topping in p_toppings:
        print(topping)
else:
    print("No pizza toppings have been chosen.")
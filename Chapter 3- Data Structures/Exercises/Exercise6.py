''' Instructions for exercise 3.6
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to 
make sure you actually have an empty list at the end of your program.'''

# Defines the list of guests
guests = ["King Solomon", "Grandma Teresita", "Mathilda"]

# Prints an invitation to the guests
print(f"Dear {guests[0]}, I'd love to hear your stories over some good food. I'd be honored to have you join us for dinner.")

print(f"Dear {guests[1]}, I've missed you so much! I'd like to invite you over for dinner at my place.")

print(f"Dear {guests[2]}, I hope you are well! It would be delightful if you were to join us for dinner.")

# Prints an apology
name = guests[1]
print(f"\nDear {guests[0]}, it seems our current schedules don't match. Let's grab a bite some other time!")

# Removes a guest
del(guests[0])

# Adds one guest
guests.insert(1, "Ms. Rafia")

# Prints the invitations again
print(f"\nDear {guests[0]}, if you're still available, plans for dinner is still on!")

print(f"Dear {guests[1]}, pleasant greetings! We're having dinner at my house, and I'd love for you to come.")

print(f"Dear {guests[2]}, dinner will be at 8, hopefully I'll see you there!")

print("\nOh no! We only have food for two guests.")

# Removes guests
name = guests.pop()
print(f"I'm so sorry {name}, let's have dinner some other time.")

# Prints formatted strings
print(f"\nDear {guests[0]}, if you're still available, plans for dinner is still on!.")

print(f"Dear {guests[1]}, see you at 8 for dinner!.")

# Removes the remaining guests
del(guests[0])
del(guests[0])

# Prints to confirm that the list is empty
print("Current guest list:", guests)

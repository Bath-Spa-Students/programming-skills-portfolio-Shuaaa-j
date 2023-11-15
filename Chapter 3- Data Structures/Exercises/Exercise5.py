''' Instructions for exercise 3.5
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.'''

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

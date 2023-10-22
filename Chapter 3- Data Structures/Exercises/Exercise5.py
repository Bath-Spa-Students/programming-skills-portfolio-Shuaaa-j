''' Instructions for exercise 3.5
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.'''


people = "King Solomon, Grandma Teresita, Kiara"
list = people.split(', ')

for person in list:
    invitation = "Dear " + person + ", if you're not busy, I'd like to invite you to dinner at my house at 8. I hope to see you there!"
    print(invitation)

guest_cant = "King Solomon"
print("\nUnfortunately, " + guest_cant + " has other plans.\n")

new_guest = "Mathilda"
list[list.index(guest_cant)] = new_guest

print("New invitation list:")
for person in list:
    invitation = "Dear " + person + ", if you're free, I'd like you to come visit me at my house for dinner at 8!"
    print(invitation)

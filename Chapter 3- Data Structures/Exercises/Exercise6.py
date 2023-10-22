''' Instructions for exercise 3.6
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''

people = "Mathilda, Grandma Teresita, Kiara"
list = people.split(', ')

for person in list:
    invitation = "Dear " + person + ", if you're not busy, I'd like to invite you to dinner at my house at 8. I hope to see you there!"
    print(invitation)

print("\n Oh my deepest apologies! I forgot the dinner table can only accommodate two guests!\n")

while len(list) > 2:
    removed_guest = list.pop()
    print("Aplogies " + removed_guest + ". I planned poorly, and it seems I invited too much people and there's not enough space. Let's have dinner some other time!")

for person in list:
    invitation = "Dear " + person + ", you can still come to dinner if you're free."
    print(invitation)

del list[-2:] 
print("Current number of peoplel on the list:", list) 



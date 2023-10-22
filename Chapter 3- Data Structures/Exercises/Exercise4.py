''' Instructions for exercise 3.4
If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d

like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.'''


people = "King Solomon, Grandma Teresita, Kiara"
list = people.split(', ')

for person in list:
    invitation = "Dear " + person + ", if you're not busy, I'd like to invite you to dinner at my house at 8. I hope to see you there!"
    print(invitation)

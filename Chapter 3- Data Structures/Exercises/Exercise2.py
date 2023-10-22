''' Instructions for exercise 3.2
Start with the list you used in Exercise 1, but instead of just

printing each person’s name, print a message to them. The text of each message should be the same, but each message should be 

personalized with the person’s name.'''


names_list = "Seif, Mariez, Samantha, Maryel, Miliani, Kiara, Adrie, Zj, Jilian"
names = names_list.split(', ')

for name in names:
    greeting = "Long time no see, " + name +  ". I missed you!"
    print(greeting)


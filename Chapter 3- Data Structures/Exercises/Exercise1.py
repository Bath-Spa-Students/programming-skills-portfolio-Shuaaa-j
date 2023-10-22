''' Instructions for exercise 3.1
Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a
time.'''

        
names_list = "Seif, Mariez, Samantha, Maryel, Miliani, Kiara, Adrie, Zj, Jilian"
names = names_list.split(', ') 

for name in names:
    print(name)
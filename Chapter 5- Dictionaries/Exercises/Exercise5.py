''' Instructions for exercise 5.5
Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. 
Next, loop through your list and asyou do, print everything you know about each pet'''


# Creates an empty list to store the dictionaries in.
pets_list = []

# Dictionaries with the information of individual pets
pet = {
    "Kind of animal": "Dog",
    "Name": "Doug",
    "Owner's name": "Joshua",
   
}
pets_list.append(pet) # Adds to the end of the list 'pets_list'

pet = {
    "Kind of animal": "Cat",
    "Name": "Kat",
    "Owner's name": "Ella",
}
pets_list.append(pet)

pet = {
    "Kind of animal": "Camel",
    "Name": "Horse",
    "Owner's name": "Seif",

}
pets_list.append(pet)

# Displays information about each pet using a loop
for pet in pets_list:
    print("\nFacts about the pets:")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))


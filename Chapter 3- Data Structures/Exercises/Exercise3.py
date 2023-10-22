''' Instructions for exercise 3.3
Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list

to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”'''


cars_list = "Toyota, Mazda, Ferarri, Bugatti, Rolls Royce"
cars = cars_list.split(', ')

for car in cars:
    statement = "I'd love to own a car that's a " + car + "."
    print(statement)

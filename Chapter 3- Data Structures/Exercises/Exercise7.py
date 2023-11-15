''' Instructions for exercise 3.7
Think of at least five places in the world you’d like to visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.

•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

•	 Use sorted() to print your list in alphabetical order without modifying the actual list.

•	 Show that your list is still in its original order by printing it.

•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

•	 Show that your list is still in its original order by printing it again.

•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.

•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.'''


# Defines a list of places
places = ["Mount Everest", "Northern Lights", "Japan", "Taj Mahal", "Baguio"]

# Print the original list of places
print("Original list of places:")
print(places)

# Prints the sorted list of places in alphabetical order 
print("\nSorted list of places in alphabetical order:")
print(sorted(places))

# Prints the original list to show that it is unchanged
print("\nOriginal list of places:")
print(places)

# Print the sorted list of places in reverse alphabetical order
print("\nSorted list of places in reverse alphabetical order:")
print(sorted(places, reverse=True))

# Print the original list to show it remains unchanged
print("\nOriginal list of places:")
print(places)

# Reverses the order of elements
places.reverse()
print("\nReversed list of places:")
print(places)

# Reverses the order of elements in the list again to restore the original order
places.reverse()
print("\nReversed list of places in original order:")
print(places)

# Sort the list in alphabetical order
places.sort()
print("\nSorted list of places in alphabetical order:")
print(places)

# Sort the list in reverse alphabetical order
places.sort(reverse=True)
print("\nSorted list of places in reverse alphabetical order:")
print(places)

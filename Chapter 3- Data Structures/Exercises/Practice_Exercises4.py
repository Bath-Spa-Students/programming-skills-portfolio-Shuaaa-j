''' Instructions for practice exercise 3.4
Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that
copies the values in numbers to numbers2.'''

# List with 100 elements using range
numbers1 = list(range(1, 101))
# Empty list
numbers2 = []

# Copy values from list 'numbers1' to list 'numbers2'
numbers2 = numbers1.copy()

# Displays the lists
print("Numbers1 list:", numbers1)
print("\nNumbers2 list:", numbers2)

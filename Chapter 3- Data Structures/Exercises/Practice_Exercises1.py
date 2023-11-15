''' Instructions for practice exercise 3.1
Given a Python list, write a program to remove all occurrences of item 20.'''


original_list = [10, 20, 30, 20, 40, 20, 50]

# While loop to remove all occurrences of 20 using del
while 20 in original_list:
    del original_list[original_list.index(20)]

# Prints the list
print("List after removing all occurences 20 from the list:", original_list)

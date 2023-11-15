''' Instructions for practice exercise 3.5
You have given a Python list. 
Write a program to find value 20 in the list, and if it is present, replace it with 200. 
Only update the first occurrence of an item.
Work with the given list: list1 = [5, 10, 15, 20, 25, 50, 20]'''

list1 = [5, 10, 15, 20, 25, 50, 20]

# Finds the first occurrence of 20 
index = None
for i, item in enumerate(list1):
    if item == 20:
        index = i
        break

# Replaces the first 20 with 200
if index is not None:
    list1[index] = 200

# Displays the updated list
print(list1)

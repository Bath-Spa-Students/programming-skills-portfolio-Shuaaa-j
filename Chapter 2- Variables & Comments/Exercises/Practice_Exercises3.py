'''Instructions for practice exercise 2.3
Write a python program that takes an input 5 from user and then type cast those values to string, int
and float in the separate variables. Print all the variables.'''

# Takes five inputs from the user
in_1 = input("Enter the first value: ")
in_2 = input("Enter the second value: ")
in_3 = input("Enter the third value: ")
in_4 = input("Enter the fourth value: ")
in_5 = input("Enter the fifth value: ")

# Typecast the inputs to string, int, and float
str_ver = str(in_1), str(in_2), str(in_3), str(in_4), str(in_5)
int_ver = int(in_1), int(in_2), int(in_3), int(in_4), int(in_5)
float_ver = float(in_1), float(in_2), float(in_3), float(in_4), float(in_5)

# Prints the variables
print("\nString variables:", str_ver)
print("Integer variables:", int_ver)
print("Float variables:", float_ver)

